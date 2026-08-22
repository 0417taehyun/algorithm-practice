# 561. Array Partition

## Problem

- [561. Array Partition](https://leetcode.com/problems/array-partition)

## Solution

### 1. Using Sort

```Python
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        answer = 0
        nums.sort()
        for idx in range(0, len(nums), 2):
            answer += min(nums[idx], nums[idx+1])

        return answer
```

- Time complexity is O(N\*logN).
- Space complexity is O(N).
