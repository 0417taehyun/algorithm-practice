# 268. Missing Number

## Problem

- [268. Missing Number](https://leetcode.com/problems/missing-number)

## Solution

### 1. Cycle Sort

```Python
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        idx = 0
        while idx < len(nums):
            if idx == nums[idx] or nums[idx] == len(nums):
                idx += 1
            else:
                nums[nums[idx]], nums[idx] = nums[idx], nums[nums[idx]]

        for idx, num in enumerate(nums):
            if idx != num:
                return idx

        return len(nums)

```

- Time complexity is O(N).
- Space complexity is O(1).
