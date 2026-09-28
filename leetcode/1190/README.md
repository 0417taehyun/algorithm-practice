# 1190. Reverse Substrings Between Each Pair of Parentheses

## Problem

- [1190. Reverse Substrings Between Each Pair of Parentheses](https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses)

## Solution

### 1. Using Stack

```Python
class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []

        for character in s:
            if character == ")":
                temp = []
                while stack and stack[-1] != "(":
                    top = stack.pop()
                    temp.append(top)

                # Remove "("
                stack.pop()
                for reversed_character in temp:
                    stack.append(reversed_character)

            else:
                stack.append(character)

        return "".join(stack)

```

- Time complexity is O(N^2).
- Space complexity is O(N).

### 2. Wormhole Teleportation Technique

```Python
class Solution:
    def reverseParentheses(self, s: str) -> str:
        pairs = {}
        stack = []
        for idx, character in enumerate(s):
            if character == "(":
                stack.append(idx)
            elif character == ")":
                open_idx = stack.pop()
                pairs[open_idx] = idx
                pairs[idx] = open_idx

        answer = []
        idx = 0
        direction = 1
        while idx < len(s):
            if s[idx] == "(" or s[idx] == ")":
                idx = pairs[idx]
                direction *= -1
            else:
                answer.append(s[idx])

            idx += direction

        return "".join(answer)

```

- Time complexity is O(N).
- Space complexity is O(N).
