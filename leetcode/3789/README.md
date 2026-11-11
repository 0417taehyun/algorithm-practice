# 3789. Minimum Cost to Acquire Required Items

## Problem

- [3789. Minimum Cost to Acquire Required Items](https://leetcode.com/problems/minimum-cost-to-acquire-required-items)

## Solution

### 1. Greedy

```Python
class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        answer = 0
        if costBoth <= (cost1 + cost2):
            used = min(need1, need2)
            answer += (costBoth * used)
            need1 -= used
            need2 -= used

            if need1 > 0:
                answer += min(costBoth*need1, cost1*need1)

            elif need2 > 0:
                answer += min(costBoth*need2, cost2*need2)

        else:
            answer += (cost1*need1 + cost2*need2)

        return answer

```

- Time complexity is O(1).
- Space complexity is O(1).
