# 1872. Stone Game VIII

## Problem

- [1872. Stone Game VIII](https://leetcode.com/problems/stone-game-viii)

## Solution

### 1. Dynamic Programming

```Python
class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)
        prefix_sum = [stones[0]] * n
        for idx in range(1, n):
            prefix_sum[idx] = prefix_sum[idx-1] + stones[idx]

        # Initialize with the case when Alice makes one move
        best = prefix_sum[-1]
        # Loop unitl 1 because if the left stones should be greater than one.
        for idx in range(n-2, 0, -1):
            # Each player plays optimally, which means they want to make the greatest gap.
            best = max(best, prefix_sum[idx]-best)

        return best
```

- Time complexity is O(N).
- Space complexity is O(N).

### 2. Space Optimization with in-place

```Python
class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)
        for idx in range(1, n):
            stones[idx] += stones[idx-1]

        best = stones[-1]
        for idx in range(n-2, 0, -1):
            best = max(best, stones[idx]-best)
        return best
```

- Time complexity is O(N).
- Space complexity is O(1).
