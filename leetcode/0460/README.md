# 460. LFU Cache

## Problem

- [460. LFU Cache](https://leetcode.com/problems/lfu-cache)

## Solution

### 1. Using Doubly Linked List

```Python
class Node:

    def __init__(
        self,
        key: int,
        value: int,
        count: int = 0,
        prev: Optional[Node] = None,
        next: Optional[Node] = None
    ):
        self.key = key
        self.value = value
        self.count = count
        self.prev = prev
        self.next = next


class Counter:

    def __init__(self):
        self.head = Node(key=-1, value=-1)
        self.tail = Node(key=-1, value=-1)
        self.head.next = self.tail
        self.tail.prev = self.head


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.minimum = 1
        self.storage: Dict[int, Node] = {}
        self.counter: Dict[int, Counter] = {}

    def get(self, key: int) -> int:
        if key not in self.storage:
            return -1

        node = self.storage[key]
        self.remove(node=node)
        self.add(node=node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.storage:
            node = self.storage[key]
            node.value = value
            self.remove(node=node)
            self.add(node=node)
            return

        if len(self.storage) == self.capacity:
            target = self.counter[self.minimum].head.next
            self.remove(node=target)
            del self.storage[target.key]

        node = Node(key=key, value=value)
        self.add(node=node)
        self.storage[key] = node

    def add(self, node: Node) -> None:
        node.count += 1
        if node.count not in self.counter:
            counter = Counter()
            self.counter[node.count] = counter
            self.minimum = min(self.minimum, node.count)

        tail = self.counter[node.count].tail
        prev = tail.prev

        prev.next = node
        node.prev = prev
        node.next = tail
        tail.prev = node

    def remove(self, node: Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

        counter = self.counter[node.count]
        if counter.head.next == counter.tail:
            del self.counter[node.count]
            if self.minimum == node.count:
                self.minimum += 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
```

- Time complexity is O(1).
- Space complexity is O(N).
