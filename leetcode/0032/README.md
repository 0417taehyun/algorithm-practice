# 32. Longest Valid Parentheses

## Problem

- [32. Longest Valid Parentheses](https://leetcode.com/problems/longest-valid-parentheses)

## Solution

### 1. Using Stack

```Python
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        answer = 0
        stack = [-1]

        for idx, character in enumerate(s):
            if character == "(":
                stack.append(idx)
            else:
                stack.pop()
                if not stack:
                    stack.append(idx)
                else:
                    answer = max(answer, idx-stack[-1])

        return answer
```

- Time complexity is O(N).
- Space complexity is O(N).
