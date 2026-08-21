# 84. Largest Rectangle in Histogram

## Problem

- [84. Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram)

## Solution

### 1. Two Pointers

> Time Limit Exceeded

```Python
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        answer = 0
        for left in range(len(heights)):
            minimum_heights = heights[left]
            for right in range(left, len(heights)):
                minimum_heights = min(minimum_heights, heights[right])
                size = (right - left + 1) * minimum_heights
                answer = max(answer, size)

        return answer

```

- Time complexity is O(N^2).
- Space complexity is O(1).

### 2. Divide and Conquer

> Time Limit Exceeded

```Python
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        def find_maximum_area(start: int, end: int) -> int:
            if start > end:
                return 0

            min_idx = start
            for idx in range(start+1, end+1):
                if heights[idx] < heights[min_idx]:
                    min_idx = idx

            current = (end - start + 1) * heights[min_idx]
            left_side = find_maximum_area(start=start, end=min_idx-1)
            right_side = find_maximum_area(start=min_idx+1, end=end)

            return max(current, left_side, right_side)


        return find_maximum_area(start=0, end=len(heights)-1)

```

> The time complexity of the worst case, sorted heights, is O(N^2),

- Time complexity is O(N\*logN).
- Space complexity is O(N).

### 3. Using Stack

```Python
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # [(left, height)]
        stack = []
        max_area = 0
        for idx, height in enumerate(heights):
            left = idx
            if stack and stack[-1][1] > height:
                while stack and stack[-1][1] > height:
                    # Keep left boundary
                    left, minimum_height = stack.pop()
                    area = (idx - left) * minimum_height
                    max_area = max(max_area, area)

            stack.append((left, height))

        while stack:
            left, minimum_height = stack.pop()
            area = (len(heights) - left) * minimum_height
            max_area = max(max_area, area)

        return max_area
```

- Time complexity is O(N).
- Space complexity is O(N).
