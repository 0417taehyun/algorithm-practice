#!/usr/bin/env python3
"""Helper for the gen-leetcode skill.

Subcommands:
  search <query>        Look up problems on LeetCode (prints JSON).
  check <id>            Show whether leetcode/<id>/ and its table row exist (prints JSON).
  create <slug>         Create leetcode/<id>/README.md and append a row to leetcode/README.md.
  touch <id> [--move]   Set the Last Solved date of an existing row to today.
  format                Re-align the table in leetcode/README.md.
"""

import argparse
import datetime
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
LEETCODE_DIR = ROOT / "leetcode"
TABLE_README = LEETCODE_DIR / "README.md"
GRAPHQL_URL = "https://leetcode.com/graphql"

QUESTION_FIELDS = "questionFrontendId title titleSlug difficulty isPaidOnly topicTags { name }"

README_TEMPLATE = """# {id}. {title}

## Problem

- [{id}. {title}](https://leetcode.com/problems/{slug})

## Solution

### 1.

```Python

```

- Time complexity is O().
- Space complexity is O().
"""


def graphql(query, variables):
    # curl instead of urllib: python.org builds on macOS often lack CA certificates.
    result = subprocess.run(
        [
            "curl", "-sS", "--fail", "--max-time", "15", GRAPHQL_URL,
            "-H", "Content-Type: application/json",
            "-H", "Referer: https://leetcode.com",
            "-H", "User-Agent: Mozilla/5.0",
            "--data-binary", "@-",
        ],
        input=json.dumps({"query": query, "variables": variables}),
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        sys.exit(f"LeetCode request failed: {result.stderr.strip()}")
    payload = json.loads(result.stdout)
    if payload.get("errors"):
        raise RuntimeError(payload["errors"])
    return payload["data"]


def search_questions(keyword, limit):
    query = (
        "query q($k: String!, $limit: Int) {"
        ' questionList(categorySlug: "", limit: $limit, skip: 0, filters: {searchKeywords: $k})'
        " { data { " + QUESTION_FIELDS + " } } }"
    )
    return graphql(query, {"k": keyword, "limit": limit})["questionList"]["data"] or []


def get_question(slug):
    query = "query q($s: String!) { question(titleSlug: $s) { " + QUESTION_FIELDS + " } }"
    return graphql(query, {"s": slug})["question"]


def simplify(question):
    return {
        "id": question["questionFrontendId"],
        "title": question["title"].strip(),
        "slug": question["titleSlug"],
        "difficulty": question["difficulty"],
        "paid_only": question["isPaidOnly"],
        "topics": [tag["name"] for tag in question["topicTags"]],
    }


def normalize(text):
    return re.sub(r"[^a-z0-9]", "", text.lower())


def cmd_search(args):
    match = re.match(r"^\s*(\d+)\s*[.)]?\s*(.*?)\s*$", args.query)
    number, title = (match.group(1), match.group(2)) if match else (None, args.query.strip())

    candidates = {}
    if number:
        for question in search_questions(number, 5):
            if question["questionFrontendId"] == number:
                candidates[question["titleSlug"]] = question
    if title:
        for question in search_questions(title, 5):
            candidates.setdefault(question["titleSlug"], question)

    results = []
    for question in candidates.values():
        item = simplify(question)
        item["number_match"] = number is not None and item["id"] == number
        item["title_match"] = bool(title) and normalize(item["title"]) == normalize(title)
        results.append(item)
    results.sort(key=lambda item: (not item["number_match"], not item["title_match"]))

    print(json.dumps({"input": {"number": number, "title": title}, "candidates": results}, ensure_ascii=False, indent=2))


def dir_name(question_id):
    return str(int(question_id)).zfill(4)


def split_row(line):
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def read_table():
    lines = TABLE_README.read_text().splitlines()
    start = next(i for i, line in enumerate(lines) if line.startswith("|"))
    end = start
    while end < len(lines) and lines[end].startswith("|"):
        end += 1
    header = split_row(lines[start])
    rows = [split_row(line) for line in lines[start + 2 : end]]
    return lines[:start], header, rows, lines[end:]


def write_table(before, header, rows, after):
    widths = [max(len(row[i]) for row in [header, *rows]) for i in range(len(header))]

    def render(cells):
        return "| " + " | ".join(cell.ljust(width) for cell, width in zip(cells, widths)) + " |"

    table = [render(header), "| " + " | ".join("-" * width for width in widths) + " |"]
    table += [render(row) for row in rows]
    TABLE_README.write_text("\n".join([*before, *table, *after]) + "\n")


def find_row(rows, question_id):
    link = f"(./{dir_name(question_id)}/README.md)"
    return next((i for i, row in enumerate(rows) if link in row[0]), None)


def cmd_check(args):
    directory = LEETCODE_DIR / dir_name(args.id)
    _, _, rows, _ = read_table()
    index = find_row(rows, args.id)
    print(
        json.dumps(
            {
                "directory": str(directory.relative_to(ROOT)),
                "directory_exists": directory.exists(),
                "readme_exists": (directory / "README.md").exists(),
                "row": " | ".join(rows[index]) if index is not None else None,
            },
            ensure_ascii=False,
            indent=2,
        )
    )


def cmd_create(args):
    question = simplify(get_question(args.slug))
    directory = LEETCODE_DIR / dir_name(question["id"])
    readme = directory / "README.md"

    before, header, rows, after = read_table()
    if readme.exists() or find_row(rows, question["id"]) is not None:
        sys.exit(f"Already exists: {readme.relative_to(ROOT)} or its table row. Run `check` first.")

    directory.mkdir(parents=True, exist_ok=True)
    readme.write_text(README_TEMPLATE.format(id=question["id"], title=question["title"], slug=question["slug"]))

    today = datetime.date.today().isoformat()
    rows.append(
        [
            f"[{question['id']}. {question['title']}](./{dir_name(question['id'])}/README.md)",
            question["difficulty"],
            ", ".join(question["topics"]),
            today,
        ]
    )
    write_table(before, header, rows, after)
    print(json.dumps({**question, "readme": str(readme.relative_to(ROOT)), "date": today}, ensure_ascii=False, indent=2))


def cmd_touch(args):
    before, header, rows, after = read_table()
    index = find_row(rows, args.id)
    if index is None:
        sys.exit(f"No table row for {args.id}.")
    row = rows.pop(index) if args.move else rows[index]
    row[-1] = datetime.date.today().isoformat()
    if args.move:
        rows.append(row)
    write_table(before, header, rows, after)
    print(" | ".join(row))


def cmd_format(_args):
    write_table(*read_table())


def main():
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(required=True)

    search = sub.add_parser("search")
    search.add_argument("query")
    search.set_defaults(func=cmd_search)

    check = sub.add_parser("check")
    check.add_argument("id")
    check.set_defaults(func=cmd_check)

    create = sub.add_parser("create")
    create.add_argument("slug")
    create.set_defaults(func=cmd_create)

    touch = sub.add_parser("touch")
    touch.add_argument("id")
    touch.add_argument("--move", action="store_true", help="also move the row to the bottom of the table")
    touch.set_defaults(func=cmd_touch)

    fmt = sub.add_parser("format")
    fmt.set_defaults(func=cmd_format)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
