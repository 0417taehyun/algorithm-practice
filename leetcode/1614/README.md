# 1614. Maximum Nesting Depth of the Parentheses

## Problem

- [1614. Maximum Nesting Depth of the Parentheses](https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses)

## Solution

### 1. Count depth

```Python
class Solution:
    def maxDepth(self, s: str) -> int:
        answer = 0
        current = 0

        for character in s:
            if character == "(":
                current += 1
            elif character == ")":
                answer = max(answer, current)
                current -= 1

        return answer

```

- Time complexity is O(N).
- Space complexity is O(1).
