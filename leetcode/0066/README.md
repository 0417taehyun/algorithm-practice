# 66. Plus One

## Problem

- [66. Plus One](https://leetcode.com/problems/plus-one)

## Solution

### 1. Using another Array

```Python
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = []
        adder = 1
        for idx in range(len(digits)-1, -1, -1):
            digits[idx] = digits[idx] + adder
            if digits[idx] >= 10:
                remainder = digits[idx] % 10
                result.append(remainder)
                adder = 1
            else:
                result.append(digits[idx])
                adder = 0

        if adder != 0:
            result.append(adder)

        return result[::-1]
```

- Time complexity is O(N).
- Space complexity is O(N).

### 2. In-pace Optimization

```Python
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for idx in range(len(digits)-1, -1, -1):
            if digits[idx] == 9:
                digits[idx] = 0
            else:
                digits[idx] += 1
                return digits

        return [1] + digits
```

- Time complexity is O(N).
- Space complexity is O(1).
