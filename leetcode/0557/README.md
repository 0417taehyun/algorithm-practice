# 557. Reverse Words in a String III

## Problem

- [557. Reverse Words in a String III](https://leetcode.com/problems/reverse-words-in-a-string-iii)

## Solution

### 1. Simulation

```Python
class Solution:
    def reverseWords(self, s: str) -> str:
        answer = []
        for word in s.split(" "):
            answer.append(word[::-1])
        return " ".join(answer)

```

- Time complexity is O(N).
- Space complexity is O(N).
