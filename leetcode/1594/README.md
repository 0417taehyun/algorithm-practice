# 1594. Maximum Non Negative Product in a Matrix

## Problem

- [1594. Maximum Non Negative Product in a Matrix](https://leetcode.com/problems/maximum-non-negative-product-in-a-matrix)

## Solution

### 1. Dynamic Programming

```Python
class Solution:
    def maxProductPath(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        min_dp = [[0] * n for _ in range(m)]
        max_dp = [[0] * n for _ in range(m)]

        for x in range(m):
            for y in range(n):
                # Base
                if x == 0 and y == 0:
                    min_dp[x][y] = grid[x][y]
                    max_dp[x][y] = grid[x][y]
                # First Row
                elif x == 0:
                    min_dp[x][y] = min(
                        min_dp[x][y-1] * grid[x][y],
                        max_dp[x][y-1] * grid[x][y]
                    )
                    max_dp[x][y] = max(
                        min_dp[x][y-1] * grid[x][y],
                        max_dp[x][y-1] * grid[x][y]
                    )
                # First Column
                elif y == 0:
                    min_dp[x][y] = min(
                        min_dp[x-1][y] * grid[x][y],
                        max_dp[x-1][y] * grid[x][y]
                    )
                    max_dp[x][y] = max(
                        min_dp[x-1][y] * grid[x][y],
                        max_dp[x-1][y] * grid[x][y]
                    )
                else:
                    min_dp[x][y] = min(
                        min_dp[x-1][y] * grid[x][y],
                        min_dp[x][y-1] * grid[x][y],
                        max_dp[x-1][y] * grid[x][y],
                        max_dp[x][y-1] * grid[x][y]
                    )
                    max_dp[x][y] = max(
                        min_dp[x-1][y] * grid[x][y],
                        min_dp[x][y-1] * grid[x][y],
                        max_dp[x-1][y] * grid[x][y],
                        max_dp[x][y-1] * grid[x][y]
                    )

        if max_dp[m-1][n-1] < 0:
            return -1

        return max_dp[m-1][n-1] % (10**9 + 7)

```

- Time complexity is O(M\*N).
- Space complexity is O(M\*N).
