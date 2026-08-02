# 1365. How Many Numbers Are Smaller Than the Current Number

## Problem

- [1365. How Many Numbers Are Smaller Than the Current Number](https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number)

## Solution

### 1. Using Map

```Python
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = {num: 0 for num in nums}
        sorted_nums = sorted(nums, reverse=True)

        total_count = len(nums)
        prev = sorted_nums[0]
        for idx, num in enumerate(sorted_nums[1:]):
            if prev > num:
                count[prev] = (total_count - 1) - idx

            prev = num

        return [ count[num] for num in nums ]

```

- Time complexity is O(NlogN).
- Space complexity is O(N).
