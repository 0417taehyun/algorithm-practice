# 64. Minimum Path Sum

## Problem

- [64. Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum)

## Solution

### 1. Dynamic Programming

```Python
class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        dp = [[0] * n for _ in range(m)]

        for x in range(m):
            for y in range(n):
                # Base
                if x == 0 and y == 0:
                    dp[x][y] = grid[x][y]
                # Edge (First Row)
                elif x == 0:
                    dp[x][y] = dp[x][y-1] + grid[x][y]
                # Edge (First Column)
                elif y == 0:
                    dp[x][y] = dp[x-1][y] + grid[x][y]
                else:
                    dp[x][y] = min(dp[x-1][y], dp[x][y-1]) + grid[x][y]

        return dp[m-1][n-1]

```

- Time complexity is O(M\*N).
- Space complexity is O(M\*N).
