# 2094. Finding 3-Digit Even Numbers

## Problem

- [2094. Finding 3-Digit Even Numbers](https://leetcode.com/problems/finding-3-digit-even-numbers)

## Solution

### 1. Using Frequency Table

```Python
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        counter = [0] * 10
        for digit in digits:
            counter[digit] += 1

        answer = []
        for number in range(100, 1000, 2):
            first, first_remainder = divmod(number, 100)
            second, third = divmod(first_remainder, 10)

            if counter[first] < 1:
                continue

            if counter[second] < 1 or (first == second and counter[second] < 2):
                continue

            if (
                counter[third] == 0
                or (first == third and counter[third] < 2)
                or (second == third and counter[third] < 2)
                or (first == second and second == third and counter[third] < 3)
            ):
                continue

            answer.append(number)

        return answer

```

- Time complexity is O(1000).
- Space complexity is O(1).
