# 131. Palindrome Partitioning

## Problem

- [131. Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning)

## Solution

### 1. Using Backtracking

```Python
class Solution:
    def partition(self, s: str) -> list[list[str]]:
        answer = []


        def dfs(s: str, partition: List[str]) -> None:
            if not s:
                answer.append(partition)
                return

            for idx in range(1, len(s)+1):
                if s[:idx] == s[:idx][::-1]:
                    dfs(s=s[idx:], partition=partition+[s[:idx]])

        dfs(s=s, partition=[])
        return answer

```

- Time complexity is O(N\*2^N).
- Space complexity is O(N).
