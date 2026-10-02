---
name: gen-leetcode
description: LeetCode 문제 이름(예. "22. Generate Parentheses")을 받아 leetcode/<4자리 번호>/README.md 풀이 템플릿을 만들고, leetcode/README.md 테이블 맨 아래에 날짜·난이도·Topic과 함께 행을 추가한다. 사용자가 LeetCode 문제를 새로 시작하거나 풀이 파일/디렉터리를 만들어 달라고 할 때 사용.
argument-hint: "<번호>. <문제 이름>"
allowed-tools: Bash(python3 .claude/skills/gen-leetcode/scripts/leetcode.py *), AskUserQuestion
---

# gen-leetcode

입력: `$ARGUMENTS` (예. `22. Generate Parentheses`)

모든 파일 작업과 LeetCode 조회는 헬퍼 스크립트로 한다. 파일이나 테이블을 직접 편집하지 말 것.
스크립트는 테이블 열 너비를 다시 맞춰 주기 때문에, 손으로 편집하면 정렬이 깨진다.

```bash
python3 .claude/skills/gen-leetcode/scripts/leetcode.py <command> ...
```

| command          | 하는 일                                                                                                       |
| ---------------- | ------------------------------------------------------------------------------------------------------------- |
| `search "<입력>"` | LeetCode를 번호와 제목으로 검색해서 후보 목록(JSON)을 출력. 후보마다 `number_match`, `title_match` 표시          |
| `check <id>`     | `leetcode/<id>/` 디렉터리, README, 테이블 행이 있는지 출력                                                     |
| `create <slug>`  | slug로 LeetCode에서 정보를 다시 받아와 README 템플릿 생성 + 테이블 맨 아래에 오늘 날짜로 행 추가 (이미 있으면 거부) |
| `touch <id> [--move]` | 기존 행의 Last Solved를 오늘 날짜로 변경. `--move`를 주면 행을 맨 아래로 이동                              |

## 절차

### 1. 입력 확인

`$ARGUMENTS`가 비어 있으면 어떤 문제인지 사용자에게 물어본다.

### 2. 문제 확정 (오타 보정)

`search`를 실행하고 결과에 따라 처리한다.

- **번호와 제목이 모두 일치하는 후보가 있다** → 그 문제로 진행한다.
- **오타로 판단된다**: 번호가 일치하는 후보가 있고 제목이 철자만 조금 다르다(예. `Genrate Parenthesis`). 또는 번호 없이 입력했는데 제목이 사실상 같은 후보가 하나뿐이다. → 그 문제로 진행하고, 마지막 보고에서 "`입력` → `보정된 이름`으로 보정했다"고 알린다.
- **그 외에는 진행하지 말고 AskUserQuestion으로 물어본다.** 예를 들면:
  - 번호가 가리키는 문제와 제목이 가리키는 문제가 다르다(예. `20. Generate Parentheses`).
  - 그럴듯한 후보가 여러 개다.
  - 후보가 없다.
  - 보정이 맞는지 확신이 서지 않는다.

  선택지에는 후보를 `번호. 제목 (난이도)` 형식으로 넣는다.

### 3. 중복 확인

`check <id>`를 실행한다. 디렉터리, README, 테이블 행 중 **하나라도** 이미 있으면 현재 상태(기존 행 내용 포함)를 보여 주고, 매번 AskUserQuestion으로 어떻게 할지 묻는다. 선택지:

- 날짜만 갱신하고 행을 맨 아래로 이동 → `touch <id> --move`
- 날짜만 갱신 (행 위치 유지) → `touch <id>`
- 중단

README가 없거나 행이 없는 등 일부만 있는 경우에는 상황을 설명하고, 빠진 부분을 어떻게 채울지 사용자에게 묻는다. 기존 README는 사용자가 명시적으로 요청하지 않으면 덮어쓰지 않는다.

### 4. 생성

`create <slug>`를 실행한다. slug는 2단계에서 확정한 후보의 `slug`이다.

- 디렉터리는 번호를 4자리로 0-패딩한 이름이다: `22` → `leetcode/0022/`
- Topic은 LeetCode 문제 페이지의 Topics 태그를 그대로 쉼표로 이어 쓴다. 태그가 없으면 빈 칸으로 둔다.
- 날짜는 로컬 기준 오늘 날짜(`YYYY-MM-DD`)이다.

### 5. 보고

다음을 짧게 알린다. git 커밋은 하지 않는다.

- 생성한 README 경로
- 테이블에 추가한 행 (난이도, Topic, 날짜)
- 오타를 보정했다면 보정 내용
