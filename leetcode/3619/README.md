# 3619. Count Islands With Total Value Divisible by K

## Problem

- [3619. Count Islands With Total Value Divisible by K](https://leetcode.com/problems/count-islands-with-total-value-divisible-by-k)

## Solution

### 1. Depth-First Search (DFS)

```Python
class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        def dfs(position: Tuple[int, int], visited: Set[Tuple[int, int]]) -> int:
            if position in visited:
                return 0

            x, y = position
            if (
                x >= len(grid)
                or x < 0
                or y >= len(grid[0])
                or y < 0
                or grid[x][y] == 0
            ):
                return 0

            visited.add(position)
            current = grid[x][y]
            x_direction = [1, 0, -1, 0]
            y_direction = [0, 1, 0, -1]
            for idx in range(4):
                new_x = x + x_direction[idx]
                new_y = y + y_direction[idx]
                current += dfs(position=(new_x, new_y), visited=visited)

            return current


        answer = 0
        visited = set()
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] != 0 and (x, y) not in visited:
                    total = dfs(position=(x, y), visited=visited)
                    if total % k == 0:
                        answer += 1

        return answer

```

- Time complexity is O(M\*N).
- Space complexity is O(M\*N).
