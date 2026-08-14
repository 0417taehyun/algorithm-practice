# 344. Reverse String

## Problem

- [344. Reverse String](https://leetcode.com/problems/reverse-string)

## Solution

### 1. Using Two Pointers

```Python
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        start = 0
        end = len(s) - 1

        while start <= end:
            temp = s[start]
            s[start] = s[end]
            s[end] = temp

            start += 1
            end -= 1

```

- Time complexity is O(N).
- Space complexity is O(1).
