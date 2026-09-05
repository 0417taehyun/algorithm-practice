# 232. Implement Queue using Stacks

## Problem

- [232. Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks)

## Solution

### 1. Using Temporary Stack

```Python
class MyQueue:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        temp = []
        while self.stack:
            temp.append(self.stack.pop())

        temp.append(x)
        while temp:
            self.stack.append(temp.pop())

    def pop(self) -> int:
        return self.stack.pop()

    def peek(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        return not self.stack


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
```

> The `push` methods takes O(N) time complexity.

- Time complexity is O(N).
- Space complexity is O(N).

### 2. Using Two Stacks

```Python
class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        self.peek()
        return self.s2.pop()

    def peek(self) -> int:
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())

        return self.s2[-1]

    def empty(self) -> bool:
        return not self.s1 and not self.s2


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

```

> The `pop` method takes amortized O(1) time complextiy.
> Since we only swap two stacks when the second stack is empty,
> it takes N times for `push`, 2N times for the first `pop`, and N-1 times for the rest of `pop`.
> Therefore, the total 4N-1 times for all 2N times operation, then O(4N-1/2N) = O(1)

- Time complexity is O(1).
- Space complexity is O(N).
