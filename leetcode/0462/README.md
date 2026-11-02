# 462. Minimum Moves to Equal Array Elements II

## Problem

- [462. Minimum Moves to Equal Array Elements II](https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii)

## Solution

### 1. Using Sort

```Python
class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        answer = 0
        nums.sort()
        mid = nums[len(nums)//2]
        for num in nums:
            answer += abs(num - mid)
        return answer

```

- Time complexity is O(N\*logN).
- Space complexity is O(1).
