# 20. Valid Parentheses

## Problem

- [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses)

## Solution

### 1. Using Stack

```Python
class Solution:
    def isValid(self, s: str) -> bool:
        group = {")": "(", "}": "{", "]": "["}

        stack = []
        for character in s:
            if stack and character in group and stack[-1] == group[character]:
                stack.pop()

            else:
                stack.append(character)

        return len(stack) == 0

```

- Time complexity is O(N).
- Space complexity is O(N).
