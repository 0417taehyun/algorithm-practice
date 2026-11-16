# 2243. Calculate Digit Sum of a String

## Problem

- [2243. Calculate Digit Sum of a String](https://leetcode.com/problems/calculate-digit-sum-of-a-string)

## Solution

### 1. Simulation

```Python
class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            temp = []
            for idx in range(0, len(s), k):
                total = 0
                for character in s[idx:idx+k]:
                    total += int(character)
                temp.append(str(total))
            s = "".join(temp)
        return s

```

- Time complexity is O(N).
- Space complexity is O(N).
