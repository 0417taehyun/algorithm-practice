# 3483. Unique 3-Digit Even Numbers

## Problem

- [3483. Unique 3-Digit Even Numbers](https://leetcode.com/problems/unique-3-digit-even-numbers/)

## Solution

### 1. Brute Force

```Python
class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        numbers = set()

        for i in range(len(digits)):
            # Pass leading zero
            if digits[i] == 0:
                continue

            for j in range(len(digits)):
                # Pass more than once
                if i == j:
                    continue

                for k in range(len(digits)):
                    # Pass more than once
                    if i == k or j == k:
                        continue

                    # Pass odd number
                    if digits[k] % 2 != 0:
                        continue

                    number = digits[i] * 100 + digits[j] * 10 + digits[k]
                    numbers.add(number)

        return len(numbers)

```

> Since the constraints of the length of digits is less than or equal to 10, it is okay to enumerate to find all possible numbers.

- Time complexity is O(N^3).
- Space complexity is O(N).
