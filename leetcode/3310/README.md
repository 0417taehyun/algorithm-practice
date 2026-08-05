# 3310. Remove Methods From Project

## Problem

- [3310. Remove Methods From Project](https://leetcode.com/problems/remove-methods-from-project)

## Solution

### 1. Depth-First Search (DFS) with Recursion

```Python
class Solution:
    def remainingMethods(
        self, n: int, k: int, invocations: List[List[int]]
    ) -> List[int]:
        # f = from, t = to
        info = {num: {"f": [], "t": []} for num in range(0, n)}
        visited = [0] * n
        suspicious = [False] * n

        for f, t in invocations:
            info[f]["t"].append(t)
            info[t]["f"].append(f)
            visited[t] += 1


        def find_bug_method_group(target_method: int) -> None:
            if suspicious[target_method]:
                return

            suspicious[target_method] = True

            for to_method in info[target_method]["t"]:
                visited[to_method] -= 1
                find_bug_method_group(target_method=to_method)


        find_bug_method_group(target_method=k)

        can_remove_all = True
        for idx in range(n):
            if suspicious[idx] and visited[idx] > 0:
                can_remove_all = False
                break

        if not can_remove_all:
            return [method for method in range(n)]

        return [method for method in range(n) if not suspicious[method]]

```

> Loop for N times to create a `info` data structure and loop for M times -the number of edges- to search.

- Time complexity is O(N+M).
- Space complexity is O(N+M).
