# 645. Set Mismatch

## Problem

- [645. Set Mismatch](https://leetcode.com/problems/set-mismatch)

## Solution

### 1. Using Map

```Python
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        count = { num: 0 for num in range(1, len(nums)+1) }

        for num in nums:
            count[num] += 1

        duplicated_number = 0
        missing_number = 0
        for num, cnt in count.items():
            if cnt == 0:
                missing_number = num

            elif cnt == 2:
                duplicated_number = num

        return [duplicated_number, missing_number]

```

- Time complexity is O(N).
- Space complexity is O(N).
