# 3348. Smallest Divisible Digit Product II

## Problem

- [3348. Smallest Divisible Digit Product II](https://leetcode.com/problems/smallest-divisible-digit-product-ii)

## Solution

### 1. Brutce Force

> Time Limit Exceeded

```Python
class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        def is_prime_number(num: int) -> bool:
            for n in range(2, int(math.sqrt(num))+1):
                if num % n == 0:
                    return False

            return True


        def is_impossible(num: int) -> bool:
            while num != 1 and num != 0:
                candidates = [2, 3, 5, 7, 9]
                for candidate in candidates:
                    if num % candidate == 0:
                        num //= candidate

                if num >= 10 and is_prime_number(num=num):
                    return True

            return False


        if is_impossible(num=t):
            return "-1"


        def check(num: str) -> bool:
            target = 1
            for digit in num:
                if int(digit) == 0:
                    return False

                target *= int(digit)

            return target % t == 0


        while not check(num=num):
            num = str(int(num)+1)

        return num


```

- Time complexity is O(N\*len(N)).
- Space complexity is O(1).

### 2. Work In Progress

```Python

```

- Time complexity is O().
- Space complexity is O(1).
