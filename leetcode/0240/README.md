# 240. Search a 2D Matrix II

## Problem

- [240. Search a 2D Matrix II](https://leetcode.com/problems/search-a-2d-matrix-ii)

## Solution

### 1. Binary Search for each rows

```Python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            left, right = 0, len(row)-1
            while left <= right:
                mid = (left + right) // 2
                if row[mid] > target:
                    right = mid -1
                elif row[mid] < target:
                    left = mid + 1
                else:
                    return True

        return False

```

- Time complexity is O(M\*logN).
- Space complexity is O(1).

### 2. Search Space Reduction

```Python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        row, column = 0, n-1
        while row < m and column >= 0:
            if matrix[row][column] < target:
                row += 1
            elif matrix[row][column] > target:
                column -= 1
            else:
                return True

        return False

```

- Time complexity is O(M+N).
- Space complexity is O(1).
