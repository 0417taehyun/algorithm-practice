# 3863. Minimum Operations to Sort a String

## Problem

- [3863. Minimum Operations to Sort a String](https://leetcode.com/problems/minimum-operations-to-sort-a-string)

## Solution

### 1. Case Analysis

```Python
class Solution:
    def minOperations(self, s: str) -> int:
        sorted_s = "".join(sorted(s))
        if sorted_s == s:
            return 0

        if len(s) == 2:
            return -1

        max_character, min_character = max(s), min(s)

        if s[0] == min_character or s[-1] == max_character:
            return 1

        for idx in range(1, len(s)-1):
            if s[idx] == min_character or s[idx] == max_character:
                return 2

        return 3

```

- Time complexity is O(NlogN).
- Space complexity is O(1).
