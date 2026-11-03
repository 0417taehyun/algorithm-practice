# 3736. Minimum Moves to Equal Array Elements III

## Problem

- [3736. Minimum Moves to Equal Array Elements III](https://leetcode.com/problems/minimum-moves-to-equal-array-elements-iii)

## Solution

### 1. Greedy

```Python
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        answer = 0
        max_num = max(nums)
        for num in nums:
            answer += (max_num - num)
        return answer

```

- Time complexity is O(N).
- Space complexity is O(1).
