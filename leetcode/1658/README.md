# 1658. Minimum Operations to Reduce X to Zero

## Problem

- [1658. Minimum Operations to Reduce X to Zero](https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero)

## Solution

### 1. Using Two Pointers to Find Maximum Subarray

```Python
class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        max_subarray = -1
        left = 0
        total = sum(nums)
        current = 0

        for right in range(len(nums)):
            current += nums[right]
            while current > (total - x) and left <= right:
                current -= nums[left]
                left += 1

            if current == (total - x):
                max_subarray = max(max_subarray, right-left+1)

        if max_subarray == -1:
            return -1

        return len(nums) - max_subarray
```

- Time complexity is O(N).
- Space complexity is O(1).
