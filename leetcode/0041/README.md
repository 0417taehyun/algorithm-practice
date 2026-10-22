# 41. First Missing Positive

## Problem

- [41. First Missing Positive](https://leetcode.com/problems/first-missing-positive)

## Solution

### 1. Cycle Sort

```Python
class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        idx = 0

        while idx < len(nums):
            correct = nums[idx] - 1

            if (
                idx == correct
                or nums[idx] >= len(nums)
                or nums[idx] <= 0
                or nums[idx] == nums[correct]
            ):
                idx += 1
            else:
                nums[correct], nums[idx] = nums[idx], nums[correct]

        for idx, num in enumerate(nums):
            if (num - 1) != idx:
                return idx + 1

        return len(nums) + 1

```

- Time complexity is O(N).
- Space complexity is O(1).
