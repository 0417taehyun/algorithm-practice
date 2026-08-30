# 2091. Removing Minimum and Maximum From Array

## Problem

- [2091. Removing Minimum and Maximum From Array](https://leetcode.com/problems/removing-minimum-and-maximum-from-array)

## Solution

### 1. Classification

```Python
class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        if len(nums) == 1 or len(nums) == 2:
            return len(nums)

        max_idx, max_num = -1, -10**6
        min_idx, min_num = -1, 10**6

        for idx, num in enumerate(nums):
            if num > max_num:
                max_num = num
                max_idx = idx

            if num < min_num:
                min_num = num
                min_idx = idx

        # Three cases
        # 1. (0 ~ First) & (First ~ Second)
        # 2. (First ~ Second) & (Second ~ N)
        # 3. (0 ~ First) & (Second ~ N)
        first = min(min_idx, max_idx)
        second = max(min_idx, max_idx)
        n = len(nums)
        return min(
            (first + 1) + (second - first),
            (second - first) + (n - second),
            (first + 1) + (n - second)
        )
```

- Time complexity is O(N).
- Space complexity is O(1).
