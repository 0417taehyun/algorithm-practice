# 28. Find the Index of the First Occurrence in a String

## Problem

- [28. Find the Index of the First Occurrence in a String](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string)

## Solution

### 1. Using Regular Expression

```Python
import re


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        result = re.search(needle, haystack)
        if result is None:
            return -1
        return result.span()[0]

```

- Time complexity is O(N).
- Space complexity is O(1).
