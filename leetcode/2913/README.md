# 2913. Subarrays Distinct Element Sum of Squares I

## Problem

- [2913. Subarrays Distinct Element Sum of Squares I](https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-i)

## Solution

### 1. Simulation

```Python
class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        answer = 0
        for i in range(len(nums)):
            count = set()
            for j in range(i, len(nums)):
                count.add(nums[j])
                answer += (len(count) ** 2)

        return answer

```

- Time complexity is O(N^2).
- Space complexity is O(N).
