# 973. K Closest Points to Origin

## Problem

- [973. K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin)

## Solution

### 1. Custom Sort

```Python
class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        return sorted(points, key=lambda point: (point[0]**2 + point[1]**2))[:k]
```

- Time complexity is O(N\*logN).
- Space complexity is O(N).
