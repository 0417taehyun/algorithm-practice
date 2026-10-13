# 3727. Maximum Alternating Sum of Squares

## Problem

- [3727. Maximum Alternating Sum of Squares](https://leetcode.com/problems/maximum-alternating-sum-of-squares)

## Solution

### 1. Sorting

```Python
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        answer = 0
        sorted_numbers = sorted(nums, key=lambda num: abs(num), reverse=True)

        middle = len(nums) // 2
        if len(nums) % 2 == 1:
            middle += 1

        answer += sum([number**2 for number in sorted_numbers[:middle]])
        answer -= sum([number**2 for number in sorted_numbers[middle:]])
        return answer

```

- Time complexity is O(NlogN).
- Space complexity is O(N).
