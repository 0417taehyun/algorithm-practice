# 75. Sort Colors

## Problem

- [75. Sort Colors](https://leetcode.com/problems/sort-colors)

## Solution

### 1. Using Bucket Sort

```Python
class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # [red, white, blue]
        colors = [0, 0, 0]
        for num in nums:
            colors[num] += 1

        idx = 0
        for num, count in enumerate(colors):
            for _ in range(count):
                nums[idx] = num
                idx += 1

```

- Time complexity is O(N).
- Space complexity is O(1).
