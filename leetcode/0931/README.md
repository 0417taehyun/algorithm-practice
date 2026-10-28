# 931. Minimum Falling Path Sum

## Problem

- [931. Minimum Falling Path Sum](https://leetcode.com/problems/minimum-falling-path-sum)

## Solution

### 1. Dynamic Programming

```Python
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])

        dp = [[0] * n for _ in range(m)]
        for x in range(m):
            for y in range(n):
                if x == 0:
                    dp[x][y] = matrix[x][y]
                else:
                    minimum = dp[x-1][y]
                    if (y - 1) >= 0:
                        minimum = min(minimum, dp[x-1][y-1])
                    if (y + 1) < n:
                        minimum = min(minimum, dp[x-1][y+1])

                    dp[x][y] = minimum + matrix[x][y]

        return min(dp[m-1])

```

- Time complexity is O(N^2).
- Space complexity is O(N^2).

### 2. Dynamic Programming with Space Optimization

```Python
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])

        prev = [num for num in matrix[0]]
        for x in range(1, m):
            curr = [0] * n
            for y in range(n):
                minimum = prev[y]
                if (y - 1) >= 0:
                    minimum = min(minimum, prev[y-1])
                if (y + 1) < n:
                    minimum = min(minimum, prev[y+1])
                curr[y] = minimum + matrix[x][y]

            prev = curr

        return min(prev)

```

- Time complexity is O(N^2).
- Space complexity is O(N).
