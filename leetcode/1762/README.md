# 1762. Buildings With an Ocean View

## Problem

- [1762. Buildings With an Ocean View](https://leetcode.com/problems/buildings-with-an-ocean-view)

## Solution

### 1. Using Stack

```Python
class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        n = len(heights)
        can_view = [True] * n
        # [index...]
        stack = []
        for idx in range(n):
            while stack and heights[stack[-1]] <= heights[idx]:
                can_view[stack.pop()] = False
            stack.append(idx)

        return [idx for idx in range(n) if can_view[idx]]

```

- Time complexity is O(N).
- Space complexity is O(N).

### 2. Space Optimization with Reversed Loop

```Python
class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        max_height = len(heights) - 1
        answer = [max_height]
        for idx in range(len(heights)-2, -1, -1):
            if heights[idx] > heights[max_height]:
                answer.append(idx)
                max_height = idx

        answer.reverse()
        return answer

```

- Time complexity is O(N).
- Space complexity is O(1).
