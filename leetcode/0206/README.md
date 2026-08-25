# 206. Reverse Linked List

## Problem

- [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list)

## Solution

### 1. Iteration

```Python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        prev_node = head
        curr_node = head.next
        head.next = None
        while curr_node is not None:
            # Reverse the next of the current node with the previous node
            temp = curr_node.next
            curr_node.next = prev_node

            # Now the current node becomes the previous node
            prev_node = curr_node

            # Now the previous next node of the current node becomes the current node
            curr_node = temp

        return prev_node

```

- Time complexity is O(N).
- Space complexity is O(1).

### 2. Recursion

```Python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        new_head = head
        if head.next:
            new_head = self.reverseList(head=head.next)
            head.next.next = head

        head.next = None
        return new_head

```

- Time complexity is O(N).
- Space complexity is O(N).
