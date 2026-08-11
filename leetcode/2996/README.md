# 2996. Smallest Missing Integer Greater Than Sequential Prefix Sum

## Problem

- [2996. Smallest Missing Integer Greater Than Sequential Prefix Sum](https://leetcode.com/problems/smallest-missing-integer-greater-than-sequential-prefix-sum)

## Solution

### 1. Using Hash Set

```Python
class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        # Find the longest sequential prefix and its sum
        seq_sum = nums[0]
        for idx in range(1, len(nums)):
            if nums[idx] - nums[idx-1] == 1:
                seq_sum += nums[idx]
            else:
                break

        # Find the smallest missing number, greater than the sum of sequnetial prefix
        num_set = set(nums)
        while seq_sum in nums_set:
            seq_sum += 1

        return seq_sum

```

- Time complexity is O(N).
- Space complexity is O(N).
