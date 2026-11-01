# 453. Minimum Moves to Equal Array Elements

## Problem

- [453. Minimum Moves to Equal Array Elements](https://leetcode.com/problems/minimum-moves-to-equal-array-elements)

## Solution

### 1. Sorting

```Python
class Solution:
    def minMoves(self, nums: list[int]) -> int:
        answer = 0
        sorted_nums = sorted(nums)
        first = sorted_nums[0]
        for idx in range(len(nums)-1, 0, -1):
            answer += (sorted_nums[idx] - first)

        return answer

```

- Time complexity is O(NlogN).
- Space complexity is O(N).

### 2. Math

```Python
class Solution:
    def minMoves(self, nums: list[int]) -> int:
        answer = 0
        min_num = min(nums)
        for num in nums:
            answer += (num - min_num)
        return answer

```

- Time complexity is O(N).
- Space complexity is O(1).
