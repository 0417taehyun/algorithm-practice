# 1475. Final Prices With a Special Discount in a Shop

## Problem

- [1475. Final Prices With a Special Discount in a Shop](https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop)

## Solution

### 1. Using Monotonic Stack

```Python
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        answer = [0] * len(prices)
        stack = []
        for idx in range(len(prices)):
            answer[idx] = prices[idx]

            while stack and prices[stack[-1]] >= prices[idx]:
                target_idx = stack.pop()
                answer[target_idx] -= prices[idx]

            stack.append(idx)

        return answer

```

- Time complexity is O(N).
- Space complexity is O(N).
