# 1401. Circle and Rectangle Overlapping

## Problem

- [1401. Circle and Rectangle Overlapping](https://leetcode.com/problems/circle-and-rectangle-overlapping)

## Solution

### 1. Calculate Distance

```Python
class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        def is_outside(x: int, y: int) -> bool:
            return ((xCenter - x) ** 2 + (yCenter - y) ** 2) ** 0.5 > radius

        x, y = xCenter, yCenter
        if x1 > xCenter:
            x = x1
        elif x2 < xCenter:
            x = x2

        if y1 > yCenter:
            y = y1
        elif y2 < yCenter:
            y = y2

        return (xCenter - x) ** 2 + (yCenter - y) ** 2 <= radius ** 2
```

- Time complexity is O(1).
- Space complexity is O(1).
