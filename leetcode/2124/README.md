# 2124. Check if All A's Appears Before All B's

## Problem

- [2124. Check if All A's Appears Before All B's](https://leetcode.com/problems/check-if-all-as-appears-before-all-bs)

## Solution

### 1. Simulation

```Python
class Solution:
    def checkString(self, s: str) -> bool:
        b_count = 0
        for character in s:
            if character == "b":
                b_count += 1
            elif character == "a" and b_count > 0:
                return False

        return True

```

- Time complexity is O(N).
- Space complexity is O(1).
