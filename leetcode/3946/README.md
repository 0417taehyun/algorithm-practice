# 3946. Maximum Number of Items From Sale I

## Problem

- [3946. Maximum Number of Items From Sale I](https://leetcode.com/problems/maximum-number-of-items-from-sale-i)

## Solution

### 1. Dynamic Programming with Greedy

```Python
class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        # [(price, copies)]
        bundles = []
        min_price = 1500
        for i in range(len(items)):
            copies = 0
            factor, price = items[i]
            for j in range(len(items)):
                if items[j][0] % factor == 0:
                    copies += 1

            bundles.append((price, copies))
            min_price = min(min_price, price)

        dp = [curr_budget // min_price for curr_budget in range(budget+1)]
        for price, copies in bundles:
            for curr_budget in range(budget, price-1, -1):
                dp[curr_budget] = max(dp[curr_budget], dp[curr_budget-price]+copies)

        return dp[budget]

```

> B refers budget

- Time complexity is O(N^2+N\*B).
- Space complexity is O(N+B).
