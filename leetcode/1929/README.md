# 1929. Concatenation of Array

## Problem

- [1929. Concatenation of Array](https://leetcode.com/problems/concatenation-of-array)

## Solution

### 1. Brute Force

```Python
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        answer = [0] * (len(nums) * 2)
        for idx in range(len(answer)):
            target_index = idx % len(nums)
            answer[idx] = nums[target_index]

        return answer

```

- Time complexity is O(2N).
- Space complexity is O(2N).
