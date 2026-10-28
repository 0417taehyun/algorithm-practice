# 3882. Minimum XOR Path in a Grid

## Problem

- [3882. Minimum XOR Path in a Grid](https://leetcode.com/problems/minimum-xor-path-in-a-grid)

## Solution

### 1. Dynamic Programming

```Python
class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[None] * n for _ in range(m)]
        for x in range(m):
            for y in range(n):
                dp[x][y] = set()
                if x == 0 and y == 0:
                    dp[x][y].add(grid[x][y])
                elif x == 0:
                    for number in list(dp[x][y-1]):
                        dp[x][y].add(number^grid[x][y])
                elif y == 0:
                    for number in list(dp[x-1][y]):
                        dp[x][y].add(number^grid[x][y])
                else:
                    for number in list(dp[x][y-1].union(dp[x-1][y])):
                        dp[x][y].add(number^grid[x][y])

        return min(dp[m-1][n-1])

```

> V refers the number of possible XOR values.

- Time complexity is O(M\*N\*V).
- Space complexity is O(M\*N\*V).
