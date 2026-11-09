# 435. Non-overlapping Intervals

## Problem

- [435. Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals)

## Solution

### 1. Using Sort with Greedy

```Python
class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x:x[1])

        answer = 0
        curr = -5*(10**4)-1
        for (start, end) in intervals:
            if start >= curr:
                curr = end
            else:
                answer += 1

        return answer

```

- Time complexity is O(N\*logN).
- Space complexity is O(N).
