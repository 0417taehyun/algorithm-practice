# 2911. Minimum Changes to Make K Semi-palindromes

## Problem

- [2911. Minimum Changes to Make K Semi-palindromes](https://leetcode.com/problems/minimum-changes-to-make-k-semi-palindromes)

## Solution

### 1. Greedy

```Python
class Solution:
    def minChanges(self, s: str) -> int:
        answer = 0
        for idx in range(0, len(s), 2):
            if s[idx] != s[idx+1]:
                answer += 1
        return answer

```

- Time complexity is O(N).
- Space complexity is O(1).
