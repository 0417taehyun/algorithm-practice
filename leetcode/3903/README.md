# 3903. Smallest Stable Index I

## Problem

- [3903. Smallest Stable Index I](https://leetcode.com/problems/smallest-stable-index-i)

## Solution

### 1. Prefix Max and Suffix Min

```Python
class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        prefix_max = []
        for num in nums:
            if not prefix_max:
                prefix_max.append(num)
            elif prefix_max[-1] >= num:
                prefix_max.append(prefix_max[-1])
            else:
                prefix_max.append(num)

        suffix_min = []
        for num in nums[::-1]:
            if not suffix_min:
                suffix_min.append(num)
            elif suffix_min[-1] <= num:
                suffix_min.append(suffix_min[-1])
            else:
                suffix_min.append(num)

        suffix_min = suffix_min[::-1]

        for idx, (max_num, min_num) in enumerate(zip(prefix_max, suffix_min)):
            if max_num - min_num <= k:
                return idx

        return -1

```

- Time complexity is O(N).
- Space complexity is O(N).
