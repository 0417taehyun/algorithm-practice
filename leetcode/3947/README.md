# 3947. Maximum Number of Items From Sale II

## Problem

- [3947. Maximum Number of Items From Sale II](https://leetcode.com/problems/maximum-number-of-items-from-sale-ii)

## Solution

### 1. Greedy with Harmonic Series

```Python
class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        factor_counter = [0] * (len(items)+1)
        for factor, _ in items:
            factor_counter[factor] += 1

        # Harmonic Series, O(NlogN)
        free_copies = [0] * len(factor_counter)
        for i in range(1, len(factor_counter)):
            # The below loop takes logN time complexity
            for j in range(i, len(factor_counter), i):
                # Skip non-exist factor
                if factor_counter[i] == 0:
                    continue
                free_copies[i] += factor_counter[j]
            # Exclude itself
            free_copies[i] -= 1

        # Ascending sort by price
        items.sort(key=lambda item: item[1])
        min_price = items[0][1]
        answer = 0
        for factor, price in items:
            # It would be better to buy minimum price item rather than buying with free copies.
            if price >= 2*min_price:
                break

            count = min(budget//price, free_copies[factor])
            budget -= (count*price)
            answer += (count*2)

        answer += (budget//min_price)
        return answer

```

- Time complexity is O(N\*logN).
- Space complexity is O(N).
