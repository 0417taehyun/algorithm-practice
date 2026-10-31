# 3665. Twisted Mirror Path Count

## Problem

- [3665. Twisted Mirror Path Count](https://leetcode.com/problems/twisted-mirror-path-count)

## Solution

### 1. Dynamic Programming

```Python
class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp_from_left = [[0] * n for _ in range(m)]
        dp_from_up = [[0] * n for _ in range(m)]

        for x in range(m):
            for y in range(n):
                if x == 0 and y == 0:
                    dp_from_left[x][y] = 1
                    continue

                if x > 0:
                    if grid[x-1][y] == 1:
                        dp_from_up[x][y] = dp_from_left[x-1][y]
                    else:
                        dp_from_up[x][y] = dp_from_left[x-1][y] + dp_from_up[x-1][y]

                if y > 0:
                    if grid[x][y-1] == 1:
                        dp_from_left[x][y] = dp_from_up[x][y-1]
                    else:
                        dp_from_left[x][y] = dp_from_up[x][y-1] + dp_from_left[x][y-1]

        return (dp_from_up[m-1][n-1] + dp_from_left[m-1][n-1]) % (10**9 + 7)
```

- Time complexity is O(M\*N).
- Space complexity is O(M\*N).
