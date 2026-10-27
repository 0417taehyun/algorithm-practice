# 3963. Create Grid With Exactly One Path

## Problem

- [3963. Create Grid With Exactly One Path](https://leetcode.com/problems/create-grid-with-exactly-one-path)

## Solution

### 1. Brute Force with One Path

```Python
class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        answer = []
        for i in range(m):
            path = []
            for j in range(n):
                if i == 0 or j == (n - 1):
                    path.append(".")
                else:
                    path.append("#")

            answer.append("".join(path))

        return answer

```

- Time complexity is O(M\*N).
- Space complexity is O(N).

### 2. Optimization

```Python
class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        answer = ["." * n]
        if m == 1:
            return answer

        left_path = "#" * (n-1) + "."
        for _ in range(m-1):
            answer.append(left_path)

        return answer

```

- Time complexity is O(M).
- Space complexity is O(N).
