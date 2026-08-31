# 3270. Find the Key of the Numbers

## Problem

- [3270. Find the Key of the Numbers](https://leetcode.com/problems/find-the-key-of-the-numbers)

## Solution

### 1. Iteration

```Python
class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        first = "0" * (4 - len(str(num1))) + str(num1)
        second = "0" * (4 - len(str(num2))) + str(num2)
        third = "0" * (4 - len(str(num3))) + str(num3)

        answer = ""
        for first_digit, second_digit, third_digit in zip(first, second, third):
            answer += str(min(int(first_digit), int(second_digit), int(third_digit)))

        return int(answer)

```

- Time complexity is O(N).
- Space complexity is O(1).
