# 147. Insertion Sort List

## Problem

- [147. Insertion Sort List](https://leetcode.com/problems/insertion-sort-list)

## Solution

### 1. Insertion Sort

```Python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode | None) -> ListNode | None:
        # Edge Case
        if head is None:
            return None

        dummy = ListNode(val=-1, next=head)
        node = head.next
        head.next = None

        while node is not None:
            next_node = node.next

            prior = dummy
            while prior.next is not None and prior.next.val > node.val:
                prior = prior.next

            node.next = prior.next
            prior.next = node

            node = next_node

        head = None
        node = dummy.next

        while node is not None:
            next_node = node.next

            node.next = head
            head = node

            node = next_node

        return head

```

- Time complexity is O(N^2).
- Space complexity is O(1).
