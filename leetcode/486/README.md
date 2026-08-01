# 486. Predict the Winner

## Problem

- [486. Predict the Winner](https://leetcode.com/problems/predict-the-winner)

## Solution

### 1. Recursion

```Python
class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        left = 0
        right = len(nums) - 1

        def get_maximum_difference(left: int, right: int, nums: List[int]) -> int:
            if left == right:
                return nums[left]

            left_score = nums[left] - get_maximum_difference(left=left+1, right=right, nums=nums)
            right_score = nums[right] - get_maximum_difference(left=left, right=right-1, nums=nums)

            return max(left_score, right_score)

        return get_maximum_difference(left=left, right=right, nums=nums) >= 0

```

- Time complexity is 2^N.
- Space complexity is N.

### 2. Dynamic Programming

```Python
class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        length = len(nums)

        memo = [[False] * length for _ in range(length)]

        left = 0
        right = length - 1

        def get_maximum_difference(left: int, right: int, nums: List[int]) -> int:
            if memo[left][right]:
                return memo[left][right]

            if left == right:
                return nums[left]

            left_score = nums[left] - get_maximum_difference(left=left+1, right=right, nums=nums)
            right_score = nums[right] - get_maximum_difference(left=left, right=right-1, nums=nums)

            memo[left][right] = max(left_score, right_score)

            return memo[left][right]

        return get_maximum_difference(left=left, right=right, nums=nums) >= 0

```

- Time complexity is N^2.
- Space complexity is N^2.
