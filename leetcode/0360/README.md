# 360. Sort Transformed Array

## Problem

- [360. Sort Transformed Array](https://leetcode.com/problems/sort-transformed-array)

## Solution

### 1. Two Pointers

```Python
class Solution:
    def sortTransformedArray(self, nums: list[int], a: int, b: int, c: int) -> list[int]:
        answer = []
        left, right = 0, len(nums) - 1

        if a >= 0:
            while left <= right:
                left_num = a*(nums[left]**2) + b*nums[left] + c
                right_num = a*(nums[right]**2) + b*nums[right] + c

                if left_num >= right_num:
                    answer.append(left_num)
                    left += 1
                else:
                    answer.append(right_num)
                    right -= 1

            answer.reverse()

        else:
            while left <= right:
                left_num = a*(nums[left]**2) + b*nums[left] + c
                right_num = a*(nums[right]**2) + b*nums[right] + c

                if left_num <= right_num:
                    answer.append(left_num)
                    left += 1
                else:
                    answer.append(right_num)
                    right -= 1

        return answer

```

- Time complexity is O(N).
- Space complexity is O(1).
