# 1140. Stone Game II

## Problem

- [1140. Stone Game II](https://leetcode.com/problems/stone-game-ii)

## Solution

### 1. Top-Down Dynamic Programming (Memoization)

> Optimized time complexity using Suffix Sum

```Python
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        memo = [[None] * len(piles) for _ in range(len(piles))] * len(piles)

        suffix_sum = [0] * (len(piles) + 1)
        for idx in range(len(piles)-1, -1, -1):
            suffix_sum[idx] = suffix_sum[idx+1] + piles[idx]


        def get_maximum_diff(start: int, m: int) -> int:
            # Return the sum of remained elements because both Alice and Bob always play optimally
            remaining = len(piles) - start
            if remaining <= 2 * m:
                return suffix_sum[start]

            if memo[start][m] is not None:
                return memo[start][m]

            # Initialize with unreachable minimum
            result = -(10**6 + 1)

            # Loop 1 <= x <= 2M
            for x in range(1, 2*m+1):
                taken = suffix_sum[start] - suffix_sum[start+x]
                diff = taken - get_maximum_diff(start=start+x, m=max(m, x))

                result = max(result, diff)

            memo[start][m] = result
            return result


        # Total sum of all the stones, which means Alice + Bob
        total = suffix_sum[0]

        # Optmized difference between Alice and Bob, which means Alice - Bob
        diff = get_maximum_diff(start=0, m=1)

        # ((Alice + Bob) + (Alice - Bob)) // 2 = (2 * Alice) // 2 = Alice
        # The difference between Alice and Bob is optimized thus the answer is optimized
        return (total + diff) // 2
```

- Time complexity is O(N^3).
- Space complexity is O(N^2).
