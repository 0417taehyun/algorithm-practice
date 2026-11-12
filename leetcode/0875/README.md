# 875. Koko Eating Bananas

## Problem

- [875. Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas)

## Solution

### 1. Using Binary Search

```Python
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        def calculate_hours(k: int) -> int:
            total = 0
            for pile in piles:
                total += (pile // k)
                if pile % k > 0:
                    total += 1
            return total


        start, end = 1, max(piles)
        answer = end
        while start <= end:
            mid = (start + end) // 2

            if calculate_hours(k=mid) > h:
                start = mid + 1
            else:
                answer = mid
                end = mid - 1

        return answer

```

- Time complexity is O(N\*logM).
- Space complexity is O(1).
