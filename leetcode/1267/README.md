# 1267. Count Servers that Communicate

## Problem

- [1267. Count Servers that Communicate](https://leetcode.com/problems/count-servers-that-communicate)

## Solution

### 1. Counting

```Python
class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        rows = [0] * m
        columns = [0] * n

        for x in range(m):
            for y in range(n):
                if grid[x][y] == 1:
                    rows[x] += 1
                    columns[y] += 1

        answer = 0
        for x in range(m):
            for y in range(n):
                if (
                    grid[x][y] == 1
                    and (
                        rows[x] >= 2
                        or columns[y] >= 2
                    )
                ):
                    answer += 1

        return answer

```

- Time complexity is O(M\*N).
- Space complexity is O(M+N).
