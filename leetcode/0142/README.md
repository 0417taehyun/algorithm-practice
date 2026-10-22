# 142. Linked List Cycle II

## Problem

- [142. Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii)

## Solution

### 1. Floyd's Tortoise and Hare

```Python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break

        if fast is None or fast.next is None:
            return None

        fast = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return fast

```

- Time complexity is O(N).
- Space complexity is O(1).
