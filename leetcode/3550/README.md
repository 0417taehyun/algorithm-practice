# 3550. Smallest Index With Digit Sum Equal to Index

## Problem

- [3550. Smallest Index With Digit Sum Equal to Index](https://leetcode.com/problems/smallest-index-with-digit-sum-equal-to-index)

## Solution

### 1. Traversal

```Python
class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for idx, num in enumerate(nums):
            digit_sum = 0
            while num > 0:
                digit_sum += num % 10
                num //= 10

            if digit_sum == idx:
                return idx

        return -1

```

- Time complexity is O(N).
- Space complexity is O(1).
