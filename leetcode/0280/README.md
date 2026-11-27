# 280. Wiggle Sort

## Problem

- [280. Wiggle Sort](https://leetcode.com/problems/wiggle-sort)

## Solution

### 1. Two Pointers

```Python
class Solution:
    def wiggleSort(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right = 0, len(nums)-1
        sorted_nums = sorted(nums)
        for idx in range(len(nums)):
            if idx % 2 == 0:
                nums[idx] = sorted_nums[left]
                left += 1
            else:
                nums[idx] = sorted_nums[right]
                right -= 1

```

- Time complexity is O(NlogN).
- Space complexity is O(N).

### 2. Greedy

```Python
class Solution:
    def wiggleSort(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for idx in range(len(nums)-1):
            if (
                (idx % 2 == 0 and nums[idx] > nums[idx+1])
                or (idx % 2 == 1 and nums[idx] < nums[idx+1])
            ):
                nums[idx], nums[idx+1] = nums[idx+1], nums[idx]

```

- Time complexity is O(N).
- Space complexity is O(1).
