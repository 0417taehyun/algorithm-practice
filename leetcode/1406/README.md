# 1406. Stone Game III

## Problem

- [1406. Stone Game III](https://leetcode.com/problems/stone-game-iii)

## Solution

### 1. Top-Down Dynamic Programming with Memoization

```Python
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [0] * (n + 1)


        def get_maximum_value(idx: int) -> int:
            if idx == n:
                return 0

            if dp[idx] != 0:
                return dp[idx]

            result = stoneValue[idx] - get_maximum_value(idx=idx+1)

            if idx + 2 <= n:
                target = (stoneValue[idx] + stoneValue[idx+1]) - get_maximum_value(idx=idx+2)
                result = max(result, target)

            if idx + 3 <= n:
                target = (stoneValue[idx] + stoneValue[idx+1] + stoneValue[idx+2]) - get_maximum_value(idx=idx+3)
                result = max(result, target)

            dp[idx] = result
            return dp[idx]


        result = get_maximum_value(idx=0)
        if result > 0:
            return "Alice"
        if result < 0:
            return "Bob"
        return "Tie"
```

- Time complexity is O(N).
- Space complexity is O(N).
