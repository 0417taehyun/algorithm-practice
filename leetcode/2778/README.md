# 2778. Sum of Squares of Special Elements

## Problem

- [2778. Sum of Squares of Special Elements](https://leetcode.com/problems/sum-of-squares-of-special-elements)

## Solution

### 1. Enumeration

```Python
class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        answer = 0
        n = len(nums)
        for idx, num in enumerate(nums, start=1):
            if n % idx == 0:
                answer += (num ** 2)
        return answer

```

- Time complexity is O(N).
- Space complexity is O(1).
