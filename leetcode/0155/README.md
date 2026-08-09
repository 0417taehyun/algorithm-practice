# 155. Min Stack

## Problem

- [155. Min Stack](https://leetcode.com/problems/min-stack)

## Solution

### 1. Using Two Stacks

```Python
class MinStack:

    def __init__(self):
        self.stack: List[int] = []
        self.min_stack: List[int] = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self) -> None:
        self.min_stack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

```

- Time complexity is O(1).
- Space complexity is O(N).

### 2. Using One Stack

```Python
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_value = 2 ** 31

    def push(self, value: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min_value = value
        else:
            diff = value - self.min_value
            self.stack.append(diff)

            if diff < 0:
                self.min_value = value

    def pop(self) -> None:
        top = self.stack.pop()

        if top < 0:
            self.min_value = self.min_value - top

    def top(self) -> int:
        top = self.stack[-1]

        if top > 0:
            return top + self.min_value

        return self.min_value

    def getMin(self) -> int:
        return self.min_value

```

- Time complexity is O(1).
- Space complexity is O(N).
