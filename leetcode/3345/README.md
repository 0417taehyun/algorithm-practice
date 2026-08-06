# 3345. Smallest Divisible Digit Product I

## Problem

- [3345. Smallest Divisible Digit Product I](https://leetcode.com/problems/smallest-divisible-digit-product-i)

## Solution

### 1. For Loop

```Python
class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def is_divisible(number: int) -> bool:
            product = 1
            while number > 0:
                product = product * (number % 10)
                number = number // 10

                # 0*N always returns 0 thus we don't need to proceed.
                if product == 0:
                    break

            return product % t == 0


        while not is_divisible(number=n):
            n += 1

        return n

```

> The answer must exist within in 10 sequential numbers and calulate the digit products take logN
> The N refers digits thus 10 \* logN equals log(N+1)

- Time complexity is O(log(N+1)).
- Space complexity is O(1).
