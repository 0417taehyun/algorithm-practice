# 50. Pow(x, n)

## Problem

- [50. Pow(x, n)](https://leetcode.com/problems/powx-n)

## Solution

### 1. Binary Exponentiation

```Python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        exponent = abs(n)
        result = 1.0

        while exponent > 0:
            if exponent % 2 == 1:
                result *= x
                exponent -= 1

            x *= x
            exponent //= 2

        if n < 0:
            return 1.0 / result

        return result

```

- Time complexity is O(logN).
- Space complexity is O(1).
