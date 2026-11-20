# 3041. Maximize Consecutive Elements in an Array After Modification

## Problem

- [3041. Maximize Consecutive Elements in an Array After Modification](https://leetcode.com/problems/maximize-consecutive-elements-in-an-array-after-modification)

## Solution

### 1. Dynamic Programming

```Python
class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        answer = 0
        dp = {}
        for num in sorted(nums):
            dp[num+1] = max(dp.get(num, 0)+1, dp.get(num+1, 0))
            dp[num] = max(dp.get(num-1, 0)+1, dp.get(num, 0))
            answer = max(answer, dp[num+1], dp[num])

        return answer

```

- Time complexity is O(N\*logN).
- Space complexity is O(N).
