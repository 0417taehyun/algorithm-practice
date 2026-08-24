# 2345. Finding the Number of Visible Mountains

## Problem

- [2345. Finding the Number of Visible Mountains](https://leetcode.com/problems/finding-the-number-of-visible-mountains)

## Solution

### 1. Using Stack with Sorted Array

```Python
class Solution:
    def visibleMountains(self, peaks: List[List[int]]) -> int:
        # Return true if peak1 can't cover the peak2.
        def is_visible(peak1: Tuple[int, int], peak2: Tuple[int, int]) -> bool:
            x1, y1 = peak1
            x2, y2 = peak2

            return (y2 - x2) > (y1 - x1) or (y2 + x2) > (y1 + x1)


        # {(x, y): count}
        counter = {}
        for peak in peaks:
            tupled_peak = tuple(peak)
            if tupled_peak not in counter:
                counter[tupled_peak] = 0
            counter[tupled_peak] += 1

        # [(x, y)]
        stack = []
        for peak in sorted(counter.keys()):
            # If the current peak covers the peak at the top of the stack, pop it.
            while stack and not is_visible(peak1=peak, peak2=stack[-1]):
                stack.pop()

            # If the peak at the top of the stack can't cover the current peak, append it.
            if not stack or is_visible(peak1=stack[-1], peak2=peak):
                stack.append(peak)

        # Remove duplicated peaks with counter
        return len([peak for peak in stack if counter[peak] == 1])

```

- Time complexity is O(N\*logN).
- Space complexity is O(N).
