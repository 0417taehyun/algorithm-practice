# 2. Add Two Numbers

## Problem

- [2. Add Two Numbers](https://leetcode.com/problems/add-two-numbers)

## Solution

### 1. Simulation

```Python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        dummy = ListNode(val=0, next=None)
        curr = dummy
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:
            l1_val = 0
            if l1 is not None:
                l1_val = l1.val

            l2_val = 0
            if l2 is not None:
                l2_val = l2.val

            total = (l1_val + l2_val + carry)
            carry = total // 10
            total = total % 10

            new_node = ListNode(val=total, next=None)
            curr.next = new_node
            curr = new_node

            if l1 is not None:
                l1 = l1.next

            if l2 is not None:
                l2 = l2.next

        return dummy.next

```

- Time complexity is O(N).
- Space complexity is O(1).
