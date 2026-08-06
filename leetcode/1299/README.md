# 1299. Replace Elements with Greatest Element on Right Side

## Problem

- [1299. Replace Elements with Greatest Element on Right Side](https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side)

## Solution

### 1. Suffix Maximum

```Python
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_num = -1

        for idx in range(len(arr)-1, -1, -1):
            temp = arr[idx]
            arr[idx] = max_num
            max_num = max(temp, max_num)

        return arr

```

- Time complexity is O(N).
- Space complexity is O(1).
