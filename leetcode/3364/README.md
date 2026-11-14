# 3364. Minimum Positive Sum Subarray

## Problem

- [3364. Minimum Positive Sum Subarray](https://leetcode.com/problems/minimum-positive-sum-subarray)

## Solution

### 1. Brute Force

```Python
class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        answer = float("inf")
        for i in range(len(nums)):
            total = 0
            for j in range(i, len(nums)):
                total += nums[j]
                if (j - i + 1) >= l and (j - i + 1) <= r and total > 0:
                    answer = min(answer, total)

        if answer == float("inf"):
            return -1

        return answer

```

- Time complexity is O(N^2).
- Space complexity is O(1).
