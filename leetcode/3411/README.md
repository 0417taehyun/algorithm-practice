# 3411. Maximum Subarray With Equal Products

## Problem

- [3411. Maximum Subarray With Equal Products](https://leetcode.com/problems/maximum-subarray-with-equal-products)

## Solution

### 1. Simulation

```Python
import math


class Solution:
    def maxLength(self, nums: List[int]) -> int:
        answer = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if math.prod(nums[i:j+1]) == math.lcm(*nums[i:j+1]) * math.gcd(*nums[i:j+1]):
                    answer = max(answer, j-i+1)
        return answer

```

- Time complexity is O(N^3).
- Space complexity is O(1).
