# 74. Search a 2D Matrix

## Problem

- [74. Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix)

## Solution

### 1. Binary Search with Two-passes

```Python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        top, bottom = 0, m-1
        while top <= bottom:
            mid = (top + bottom) // 2
            if matrix[mid][0] > target:
                bottom = mid - 1
            elif matrix[mid][n-1] < target:
                top = mid + 1
            else:
                break

        if top > bottom:
            return False

        row = (top + bottom) // 2
        left, right = 0, n-1
        while left <= right:
            mid = (left + right) // 2
            if matrix[row][mid] > target:
                right = mid - 1
            elif matrix[row][mid] < target:
                left = mid + 1
            else:
                return True

        return False

```

- Time complexity is O(logM\*N).
- Space complexity is O(1).

### 2. Binary Search with One-pass

```Python
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        start, end = 0, m*n-1

        while start <= end:
            mid = (start + end) // 2
            row = mid // n
            column = mid % n

            if matrix[row][column] > target:
                end = mid - 1
            elif matrix[row][column] < target:
                start = mid + 1
            else:
                return True

        return False

```

- Time complexity is O(logM\*N).
- Space complexity is O(1).
