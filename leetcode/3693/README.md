# 3693. Climbing Stairs II

## Problem

- [3693. Climbing Stairs II](https://leetcode.com/problems/climbing-stairs-ii)

## Solution

### 1. Dynamic Programming

```Python
class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp = [0]
        for idx, cost in enumerate(costs, start=1):
            min_cost = dp[idx-1] + cost + 1

            if (idx - 2) >= 0:
                min_cost = min(min_cost, dp[idx-2] + cost + 4)

            if (idx - 3) >= 0:
                min_cost = min(min_cost, dp[idx-3] + cost + 9)

            dp.append(min_cost)

        return dp[-1]

```

- Time complexity is O(N).
- Space complexity is O(N).

### 2. Space Optimization

```Python
class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        prev3, prev2, prev1 = 0, 0, 0
        for idx in range(n):
            prev3, prev2, prev1 = prev2, prev1, min(prev3+9, prev2+4, prev1+1)+costs[idx]
        return prev1

```

- Time complexity is O(N).
- Space complexity is O(1).
