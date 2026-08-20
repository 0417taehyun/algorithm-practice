# 3069. Distribute Elements Into Two Arrays I

## Problem

- [3069. Distribute Elements Into Two Arrays I](https://leetcode.com/problems/distribute-elements-into-two-arrays-i)

## Solution

### 1. Brute Force

```Python
class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1 = []
        arr2 = []
        for idx, num in enumerate(nums, start=1):
            if idx == 1:
                arr1.append(num)
            elif idx == 2:
                arr2.append(num)
            elif arr1[-1] > arr2[-1]:
                arr1.append(num)
            else:
                arr2.append(num)

        return arr1 + arr2


```

- Time complexity is O(N).
- Space complexity is O(N).
