# 2058. Find the Minimum and Maximum Number of Nodes Between Critical Points

## Problem

- [2058. Find the Minimum and Maximum Number of Nodes Between Critical Points](https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points)

## Solution

### 1. Iteration

```Python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev = None
        node = head
        index = 0
        critical_points = []
        while node is not None:
            if prev is not None and node.next is not None:
                # Local maxima
                if node.val > prev.val and node.val > node.next.val:
                    critical_points.append(index)
                # Local minima
                elif node.val < prev.val and node.val < node.next.val:
                    critical_points.append(index)

            prev = node
            node = node.next
            index += 1

        if len(critical_points) < 2:
            return [-1, -1]

        max_distance = critical_points[-1] - critical_points[0]
        min_distance = critical_points[-1] - critical_points[0]
        for idx in range(1, len(critical_points)):
            min_distance = min(critical_points[idx] - critical_points[idx-1], min_distance)

        return [min_distance, max_distance]
```

- Time complexity is O(N).
- Space complexity is O(N).
