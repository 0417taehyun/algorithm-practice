# 3904. Smallest Stable Index II

## Problem

- [3904. Smallest Stable Index II](https://leetcode.com/problems/smallest-stable-index-ii)

## Solution

### 1. Prefix Max and Suffix Min

```Python
class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        prefix_max = []
        for num in nums:
            if not prefix_max or prefix_max[-1] < num:
                prefix_max.append(num)
            else:
                prefix_max.append(prefix_max[-1])

        suffix_min = []
        for num in nums[::-1]:
            if not suffix_min or suffix_min[-1] >= num:
                suffix_min.append(num)
            else:
                suffix_min.append(suffix_min[-1])

        for idx, (max_num, min_num) in enumerate(zip(prefix_max, suffix_min[::-1])):
            if (max_num - min_num) <= k:
                return idx

        return -1
```

- Time complexity is O(N).
- Space complexity is O(N).
