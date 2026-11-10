# 746. Min Cost Climbing Stairs

## Problem

- [746. Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs)

## Solution

### 1. Dynamic Programming

```Python
class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        step1, step2 = 0, 0
        for idx in range(len(cost)):
            step1, step2 = step2, min(step1, step2) + cost[idx]

        return min(step1, step2)

```

- Time complexity is O(N).
- Space complexity is O(1).
