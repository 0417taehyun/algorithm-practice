# 1021. Remove Outermost Parentheses

## Problem

- [1021. Remove Outermost Parentheses](https://leetcode.com/problems/remove-outermost-parentheses)

## Solution

### 1. Counting the depth

```Python
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        answer = []
        curr_depth = 0

        for character in s:
            if character == "(":
                if curr_depth > 0:
                    answer.append(character)
                curr_depth += 1
            else:
                curr_depth -= 1
                if curr_depth > 0:
                    answer.append(character)

        return "".join(answer)

```

- Time complexity is O(N).
- Space complexity is O(1).
