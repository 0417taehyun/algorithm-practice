# 707. Design Linked List

## Problem

- [707. Design Linked List](https://leetcode.com/problems/design-linked-list)

## Solution

### 1. Desing Linked List

```Python
class Node:
    def __init__(self, value: int, next: Optional["Node"] = None):
        self.value = value
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None

    def get(self, index: int) -> int:
        count = 0
        node = self.head
        while node is not None:
            if count == index:
                return node.value
            count += 1
            node = node.next
        return -1

    def addAtHead(self, val: int) -> None:
        node = Node(value=val, next=self.head)
        if self.head is None:
            # Empty Linked List
            self.tail = node
        self.head = node

    def addAtTail(self, val: int) -> None:
        node = Node(value=val)
        if self.tail is None:
            # Empty Linked List
            self.head = node
        else:
            # Update the next node of the previous tail node.
            self.tail.next = node
        self.tail = node

    def addAtIndex(self, index: int, val: int) -> None:
        # Add at head
        if index == 0:
            self.addAtHead(val=val)
            return

        count = 0
        node = self.head
        while node is not None and count < (index - 1):
            count += 1
            node = node.next

        # Index is greater than the length of the Linked List
        if node is None:
            return

        # Add at tail
        if node.next is None:
            self.addAtTail(val=val)
            return

        new_node = Node(value=val, next=node.next)
        node.next = new_node


    def deleteAtIndex(self, index: int) -> None:
        # Cannot delete anything because Linked List is empty
        if self.head is None:
            return

        # Delete at head
        if index == 0:
            # Delete both head and tail because the Linked List becomes empty
            if self.head.next is None:
                self.tail = None
            self.head = self.head.next
            return

        count = 0
        node = self.head
        while node is not None and count < (index - 1):
            count += 1
            node = node.next

        # Index is greater than the length of the Linked List
        if node is None or node.next is None:
            return

        node.next = node.next.next

        # Update tail
        if node.next is None:
            self.tail = node


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

```
