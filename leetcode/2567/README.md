# 2567. Minimum Score by Changing Two Elements

## Problem

- [2567. Minimum Score by Changing Two Elements](https://leetcode.com/problems/minimum-score-by-changing-two-elements)

## Solution

### 1. Simulation

```Python
class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        max_nums, min_nums = [0, 0, 0], [10**9+1, 10**9+1, 10**9+1]
        for num in nums:
            max_nums.append(num)
            max_nums.sort(reverse=True)
            max_nums.pop()

            min_nums.append(num)
            min_nums.sort()
            min_nums.pop()

        return min(
            max_nums[0]-min_nums[-1],
            max_nums[-1]-min_nums[0],
            max_nums[1]-min_nums[1]
        )

```

> We only manage the fixed size array, thus we ignore the constant complexity

- Time complexity is O(N).
- Space complexity is O(1).
