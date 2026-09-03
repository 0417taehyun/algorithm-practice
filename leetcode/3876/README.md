# 3876. Construct Uniform Parity Array II

## Problem

- [3876. Construct Uniform Parity Array II](https://leetcode.com/problems/construct-uniform-parity-array-ii)

## Solution

### 1. Math

```Python
class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        min_num = min(nums1)
        is_min_num_odd = True
        if min_num % 2 == 0:
            is_min_num_odd = False

        if is_min_num_odd:
            return True

        for num in nums1:
            if num % 2 == 1:
                return False

        return True
```

- Time complexity is O(N).
- Space complexity is O(1).
