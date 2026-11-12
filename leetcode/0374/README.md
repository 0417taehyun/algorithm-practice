# 374. Guess Number Higher or Lower

## Problem

- [374. Guess Number Higher or Lower](https://leetcode.com/problems/guess-number-higher-or-lower)

## Solution

### 1. Using Binary Search

```Python
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        start = 1
        while start <= n:
            mid = (start + n) // 2
            if guess(mid) > 0:
                start = mid + 1
            elif guess(mid) < 0:
                n = mid - 1
            else:
                return mid
```

- Time complexity is O(logN).
- Space complexity is O(1).
