# 21. Merge Two Sorted Lists

## Problem

- [21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists)

## Solution

### 1. In-place Iteration

```Python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None

        head = None
        if list1 is None:
            head = list2
        elif list2 is None:
            head = list1
        elif list1.val <= list2.val:
            head = list1
        else:
            head = list2

        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                while list1.next is not None and list1.next.val <= list2.val:
                    list1 = list1.next

                temp = list1.next
                list1.next = list2
                list2 = temp
                list1 = list1.next
            else:
                while list2.next is not None and list2.next.val <= list1.val:
                    list2 = list2.next

                temp = list2.next
                list2.next = list1
                list1 = temp
                list2 = list2.next

        return head

```

- Time complexity is O(N).
- Space complexity is O(1).

### 2. Iteration with Dummy Node

```Python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode()

        prev_node = dummy_head
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                prev_node.next = list1
                list1 = list1.next
            else:
                prev_node.next = list2
                list2 = list2.next

            prev_node = prev_node.next

        if list1 is not None:
            prev_node.next = list1
        else:
            prev_node.next = list2

        return dummy_head.next

```

- Time complexity is O(N).
- Space complexity is O(1).

### 3. Recursion

```Python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        elif list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1=list1.next, list2=list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1=list1, list2=list2.next)
            return list2

```

- Time complexity is O(N).
- Space complexity is O(N).
