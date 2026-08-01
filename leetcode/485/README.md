# 485. Max Consecutive Ones

## Problem

- [485. Max Consecutive Ones](https://leetcode.com/problems/max-consecutive-ones)

## Solution

### 1. Brute Force

```Python
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maximum = 0
        current = 0

        for num in nums:
            if num == 1:
                current += 1
            else:
                maximum = max(maximum, current)
                current = 0

        return max(maximum, current)
```

- Time complexity is O(N).
- Space complexity is O(1).
