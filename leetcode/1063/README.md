# 1063. Number of Valid Subarrays

## Problem

- [1063. Number of Valid Subarrays](https://leetcode.com/problems/number-of-valid-subarrays)

## Solution

### 1. Using Stack

```Python
class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        # [index...]
        stack = []
        answer = 0
        n = len(nums)
        for idx in range(n):
            while stack and nums[stack[-1]] > nums[idx]:
                answer += (idx - stack.pop())
            stack.append(idx)

        while stack:
            answer += (n - stack.pop())

        return answer

```

- Time complexity is O(N).
- Space complexity is O(N).
