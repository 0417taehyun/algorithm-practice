# 3644. Maximum K to Sort a Permutation

## Problem

- [3644. Maximum K to Sort a Permutation](https://leetcode.com/problems/maximum-k-to-sort-a-permutation)

## Solution

### 1. Bit Manipulation

```Python
class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        answer = -1

        for idx, num in enumerate(nums):
            if idx == num:
                continue
            answer &= num

        if answer == -1:
            return 0

        return answer

```

- Time complexity is O(N).
- Space complexity is O(1).
