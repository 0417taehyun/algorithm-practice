# 3622. Check Divisibility by Digit Sum and Product

## Problem

- [3622. Check Divisibility by Digit Sum and Product](https://leetcode.com/problems/check-divisibility-by-digit-sum-and-product)

## Solution

### 1. Simulation

```Python
class Solution:
    def checkDivisibility(self, n: int) -> bool:
        target = n
        sum_num = 0
        product_num = 1
        while target > 0:
            remainder = (target % 10)
            sum_num += remainder
            product_num *= remainder
            target //= 10
        return n % (sum_num + product_num) == 0
```

- Time complexity is O(logN).
- Space complexity is O(1).
