# 324. Wiggle Sort II

## Problem

- [324. Wiggle Sort II](https://leetcode.com/problems/wiggle-sort-ii)

## Solution

### 1. Bucket Sort

```Python
class Solution:
    def wiggleSort(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        bucket = [0] * (max(nums) + 1)
        for num in nums:
            bucket[num] += 1

        num = len(bucket) - 1

        for start in (1, 0):
            for idx in range(start, len(nums), 2):
                while bucket[num] == 0:
                    num -= 1
                nums[idx] = num
                bucket[num] -= 1
```

> Since 0 <= nums[i] <= 5000, we can assume that space complexity is constant.

- Time complexity is O(N).
- Space complexity is O(1).
