# 856. Score of Parentheses

## Problem

- [856. Score of Parentheses](https://leetcode.com/problems/score-of-parentheses)

## Solution

### 1. Calculate Depth

```Python
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        answer = 0
        depth = 0
        for idx, character in enumerate(s):
            if character == "(":
                depth += 1
            else:
                depth -= 1
                if s[idx-1] == "(":
                    answer += (2 ** depth)
        return answer

```

- Time complexity is O(N).
- Space complexity is O(1).
