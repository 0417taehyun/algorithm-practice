# 179. Largest Number

## Problem

- [179. Largest Number](https://leetcode.com/problems/largest-number)

## Solution

### 1. Using Custom Sort

```Python
from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # If (a + b) > (b + a), then c + (a + b) > c + (b + a) and (a + b) + c > (b + a) + c.
        # For example if a is "3" and b is "30", (a + b) is "330" and (b + a) is "303", thus (a + b) > (b + a).
        # If c is "9", then "9330" > "9303" and also "3309" > "3039".
        def compare(first: str, second: str):
            if first + second > second + first:
                return -1
            if first + second < second + first:
                return 1
            return 0

        has_all_zero = True
        for idx in range(len(nums)):
            if nums[idx] != 0:
                has_all_zero = False
            nums[idx] = str(nums[idx])

        # Handle edge cases, such as [0, 0, 0]
        if has_all_zero:
            return "0"

        nums.sort(key=cmp_to_key(compare))
        return "".join(nums)

```

> K refers the length of number and the maximum K is 9 since the constraint, 0 <= nums[i] <= 10^9

- Time complexity is O(K\*N\*logN).
- Space complexity is O(1).
