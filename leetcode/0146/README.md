# 146. LRU Cache

## Problem

- [146. LRU Cache](https://leetcode.com/problems/lru-cache)

## Solution

### 1. Using Doubly Linked List

```Python
class Node:

    def __init__(
        self,
        key: int,
        value: int,
        prev_node: Optional[Node] = None,
        next_node: Optional[Node] = None,
    ):
        self.key = key
        self.value = value
        self.prev = prev_node
        self.next = next_node


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity

        # {key: Node}
        self.storage = {}

        # Dummies
        self.head = Node(key=-1, value=-1)
        self.tail = Node(key=-1, value=-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.storage:
            return -1

        node = self.storage[key]
        self.remove(node=node)
        self.add(node=node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.storage:
            prev_node = self.storage[key]
            self.remove(node=prev_node)

        node = Node(key=key, value=value)
        self.add(node=node)
        self.storage[key] = node

        if len(self.storage) > self.capacity:
            target = self.head.next
            self.remove(node=target)
            del self.storage[target.key]

    def add(self, node: Node) -> None:
        prev_node = self.tail.prev
        prev_node.next = node
        self.tail.prev = node
        node.prev = prev_node
        node.next = self.tail

    def remove(self, node: Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
```

> N refers capacity

- Time complexity is O(N).
- Space complexity is O(1).
