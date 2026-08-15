# 819. Most Common Word

## Problem

- [819. Most Common Word](https://leetcode.com/problems/most-common-word)

## Solution

### 1. Using Hash Map

```Python
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        counter = {}
        banned_words = set(banned)
        normalized_paragraph = re.sub(r"[^\w]", ' ', paragraph)
        for word in normalized_paragraph.split(" "):
            normalized_word = word.lower()
            if normalized_word.isalpha() and normalized_word not in banned_words:
                if normalized_word in counter:
                    counter[normalized_word] += 1
                else:
                    counter[normalized_word] = 1

        answer = ""
        max_count = 0
        for word, count in counter.items():
            if count > max_count:
                answer = word
                max_count = count

        return answer

```

- Time complexity is O(N).
- Space complexity is O(N).
