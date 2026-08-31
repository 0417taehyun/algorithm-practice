# 225. Implement Stack using Queues

## Problem

- [225. Implement Stack using Queues](https://leetcode.com/problems/implement-stack-using-queues)

## Solution

### 1. Using One Queue

```Python
class Node:

    def __init__(self, x: int, prev: Optional["Node"] = None, next: Optional["Node"] = None):
        self.x = x
        self.prev = prev
        self.next = next


class Queue:
    def __init__(self):
        self.size = 0
        self.head = Node(x=0)
        self.tail = Node(x=0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def push(self, x: int) -> None:
        node = Node(x=x, prev=self.tail.prev, next=self.tail)
        self.tail.prev.next = node
        self.tail.prev = node
        self.size += 1

    def pop(self) -> int:
        if self.empty():
            return -1

        x = self.head.next.x
        self.head.next.next.prev = self.head
        self.head.next = self.head.next.next
        self.size -= 1
        return x

    def peek(self) -> int:
        if self.empty():
            return -1

        return self.head.next.x

    def empty(self) -> bool:
        return self.size == 0


class MyStack:

    def __init__(self):
        self.queue = Queue()

    def push(self, x: int) -> None:
        count = 0
        size = self.queue.size
        self.queue.push(x=x)
        while count < size:
            peek = self.queue.pop()
            self.queue.push(x=peek)
            count += 1

    def pop(self) -> int:
        return self.queue.pop()

    def top(self) -> int:
        return self.queue.peek()

    def empty(self) -> bool:
        return self.queue.empty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
```

### 2. Using Queue of Queues

> The code below violates the restriction.
> _The code uses a recursive list/deque structure to simulate a stack rather than using the container as a FIFO queue._
> However, the time complexity of all operations is O(1).

```Python
class MyStack:

    def __init__(self):
        self.queue = None

    def push(self, x: int) -> None:
        # [top, self.queue]
        # [0, 1]
        # [x, [x, [x, None]]]
        self.queue = deque([x, self.queue])

    def pop(self) -> int:
        top = self.queue.popleft()
        self.queue = self.queue.popleft()
        return top

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return not self.queue


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
```
