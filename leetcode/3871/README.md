# 3871. Count Commas in Range II

## Problem

- [3871. Count Commas in Range II](https://leetcode.com/problems/count-commas-in-range-ii)

## Solution

### 1. Calculation

```Python
class Solution:
    def countCommas(self, n: int) -> int:
        if n < 1000:
            return 0

        count = 1
        base, curr = 1000, 1000**2
        answer = 0
        while base <= n:
            if curr > n:
                answer += ((n - base + 1) * count)

            else:
                answer += ((curr - base) * count)

            base *= 1000
            curr *= 1000
            count += 1

        return answer

```

- Time complexity is O(logN).
- Space complexity is O(1).

### 2. Simpler Calculation

```Python
class Solution:
    def countCommas(self, n: int) -> int:
        base = 1000
        answer = 0

        while base <= n:
            answer += (n - base + 1)
            base *= 1000

        return answer

```

- Time complexity is O(logN).
- Space complexity is O(1).
