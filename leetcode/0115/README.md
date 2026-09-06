# 115. Distinct Subsequences

## Problem

- [115. Distinct Subsequences](https://leetcode.com/problems/distinct-subsequences)

## Solution

### 1. Recursion with Memoization

```Python
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        visited = {}


        def dfs(s_idx: int, t_idx: int) -> int:
            # Find a single subsequence
            if t_idx == len(t):
                return 1

            # Find nothing
            if s_idx == len(s):
                return 0

            # Use memoization
            if (s_idx, t_idx) in visited:
                return visited[(s_idx, t_idx)]

            count = dfs(s_idx=s_idx+1, t_idx=t_idx)
            if s[s_idx] == t[t_idx]:
                count += dfs(s_idx=s_idx+1, t_idx=t_idx+1)

            visited[(s_idx, t_idx)] = count
            return count


        return dfs(s_idx=0, t_idx=0)

```

- Time complexity is O(N^2).
- Space complexity is O(N^2).
