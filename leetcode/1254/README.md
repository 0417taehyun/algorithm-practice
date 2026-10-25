# 1254. Number of Closed Islands

## Problem

- [1254. Number of Closed Islands](https://leetcode.com/problems/number-of-closed-islands)

## Solution

### 1. Depth-First Search (DFS)

```Python
class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        def dfs(position: Tuple[int, int], visited: Set[Tuple[int, int]]) -> bool:
            x, y = position

            # Out of grid
            if (
                x < 0
                or x >= len(grid)
                or y < 0
                or y >= len(grid[0])
            ):
                return False

            # Closed
            if grid[x][y] == 1 or position in visited:
                return True

            visited.add(position)

            is_closed = True
            x_directions = [0, 1, 0, -1]
            y_directions = [1, 0, -1, 0]
            for idx in range(4):
                new_x = x + x_directions[idx]
                new_y = y + y_directions[idx]

                if not dfs(position=(new_x, new_y), visited=visited):
                    is_closed = False

            return is_closed


        answer = 0
        visited = set()
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if (
                    grid[x][y] == 0
                    and (x, y) not in visited
                    and dfs(position=(x, y), visited=visited)
                ):
                    answer += 1

        return answer

```

- Time complexity is O(N\*M).
- Space complexity is O(N\*M).
