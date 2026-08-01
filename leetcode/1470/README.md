# 1470. Shuffle the Array

## Problem

- [1470. Shuffle the Array](https://leetcode.com/problems/shuffle-the-array)

## Solution

### 1. Brute Force

```Python
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        answer = []
        for idx in range(n):
            answer.append(nums[idx])
            answer.append(nums[idx+n])

        return answer

```

- Time complexity is N.
- Space complexity is N.
