# 1295. Find Numbers with Even Number of Digits

## Problem

- [1295. Find Numbers with Even Number of Digits](https://leetcode.com/problems/find-numbers-with-even-number-of-digits)

## Solution

### 1. Brute Force

```Python
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        answer = 0
        for num in nums:
            count = 0
            while num >= 1:
                num, digit = divmod(num, 10)
                count += 1

            if count % 2 == 0:
                answer += 1

        return answer

```

> M refers the length of number.

- Time complexity is O(N\*logM).
- Space complexity is O(1).

### 2. Range Classification

```Python
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        answer = 0
        for num in nums:
            if (
                (num >= 10 and num < 100)
                or (num >= 1000 and num < 10000)
                or (num >= 100000 and num < 1000000)
            ):
                answer += 1

        return answer

```

- Time complexity is O(N).
- Space complexity is O(1).
