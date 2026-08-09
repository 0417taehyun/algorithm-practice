# 150. Evaluate Reverse Polish Notation

## Problem

- [150. Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation)

## Solution

### 1. Using Stack

```Python
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def calculate(left: int, right: int, operation: str) -> int:
            if operation == "+":
                return left + right
            if operation == "-":
                return left - right
            if operation == "*":
                return left * right

            return int(left / right)

        operations = {"+", "-", "*", "/"}
        numbers = []
        for token in tokens:
            if token in operations:
                right = numbers.pop()
                left = numbers.pop()
                result = calculate(left=left, right=right, operation=token)
                numbers.append(result)
            else:
                numbers.append(int(token))

        return numbers.pop()

```

- Time complexity is O(N).
- Space complexity is O(N).
