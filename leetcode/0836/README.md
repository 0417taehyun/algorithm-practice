# 836. Rectangle Overlap

## Problem

- [836. Rectangle Overlap](https://leetcode.com/problems/rectangle-overlap)

## Solution

### 1. Classification

```Python
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x1, y1, x2, y2 = rec1
        x3, y3, x4, y4 = rec2

        if (
            x3 > x2
            or x4 < x1
            or y3 > y2
            or y4 < y1
            or x2 == x3
            or x1 == x4
            or y2 == y3
            or y1 == y4
        ):
            return False

        return True

```

- Time complexity is O(1).
- Space complexity is O(1).
