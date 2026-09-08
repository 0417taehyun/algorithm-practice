# 3870. Count Commas in Range

## Problem

- [3870. Count Commas in Range](https://leetcode.com/problems/count-commas-in-range)

## Solution

### 1. Calculation

```Python
class Solution:
    def countCommas(self, n: int) -> int:
        if n < 1000:
            return 0

        return (n - 1000) + 1

```

- Time complexity is O(1).
- Space complexity is O(1).
