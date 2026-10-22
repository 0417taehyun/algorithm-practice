# 442. Find All Duplicates in an Array

## Problem

- [442. Find All Duplicates in an Array](https://leetcode.com/problems/find-all-duplicates-in-an-array)

## Solution

### 1. Cycle Sort

```Python
class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        idx = 0
        while idx < len(nums):
            correct  = nums[idx] - 1
            if (
                idx == correct
                or nums[idx] == nums[correct]
            ):
                idx += 1
            else:
                nums[idx], nums[correct] = nums[correct], nums[idx]

        answer = []
        for idx, num in enumerate(nums):
            if (num - 1) != idx:
                answer.append(num)

        return answer

```

- Time complexity is O(N).
- Space complexity is O(1).
