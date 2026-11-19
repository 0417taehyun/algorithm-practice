# 372. Super Pow

## Problem

- [372. Super Pow](https://leetcode.com/problems/super-pow)

## Solution

### 1. Binary Exponentiation

```Python
class Solution:
    def superPow(self, a: int, b: list[int]) -> int:
        MOD = 1337


        def pow(a: int, n: int) -> int:
            result = 1
            while n > 0:
                if n % 2 == 1:
                    result = result * a % MOD
                    n -=1

                a = a * a % MOD
                n //= 2

            return result


        n = 0
        digits = len(b)-1
        for number in b:
            n += (number * (10**digits))
            digits -= 1

        return pow(a=a, n=n)

```

> N is a sum of elements in array b

- Time complexity is O(logN).
- Space complexity is O(1).

### 2. Left-to-Right Exponentiation

```Python
class Solution:
    def superPow(self, a: int, b: list[int]) -> int:
        MOD = 1337

        a %= MOD
        answer = 1
        for digit in b:
            answer = pow(answer, 10, MOD) * pow(a, digit, MOD) % MOD

        return answer

```

> N is a number of elements in array b

- Time Complexity is O(N)
- Space Complexity is O(1)
