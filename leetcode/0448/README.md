# 448. Find All Numbers Disappeared in an Array

## Problem

- [448. Find All Numbers Disappeared in an Array](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array)

## Solution

### 1. Brute Force

```Python
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        count = [0] * len(nums)

        for num in nums:
            count[num-1] += 1

        return [ num+1 for num, cnt in enumerate(count) if cnt == 0 ]
```

- Time complexity is O(N).
- Space complexity is O(N).
