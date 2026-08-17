# 1563. Stone Game V

## Problem

- [1563. Stone Game V](https://leetcode.com/problems/stone-game-v)

## Solution

### 1. Top-Down Dynamic Programming (Memoization)

> Optimized time complexity using Prefix Sum

```Python
class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        memo = [[-1] * (len(stoneValue) + 1) for _ in range(len(stoneValue) + 1)]

        # Use prefix sum not to loop for calculate the sum
        prefix_sum = [0] * (len(stoneValue) + 1)
        for idx, stone in enumerate(stoneValue):
            prefix_sum[idx + 1] = prefix_sum[idx] + stone


        def find_maximum_score(start: int, end: int) -> int:
            # Only one stone left
            if end - start == 1:
                return 0

            if memo[start][end] != -1:
                return memo[start][end]

            best = 0
            for pointer in range(start+1, end):
                total = 0

                # O(1) time complexity due to the prefix sum
                left_sum = prefix_sum[pointer] - prefix_sum[start]
                right_sum = prefix_sum[end] - prefix_sum[pointer]

                if left_sum > right_sum:
                    total += right_sum + find_maximum_score(start=pointer, end=end)
                elif left_sum < right_sum:
                    total += left_sum + find_maximum_score(start=start, end=pointer)

                # Choose the maximum if the sum(left) == sum(right)
                else:
                    total += (
                        left_sum
                        + max(
                            find_maximum_score(start=start, end=pointer),
                            find_maximum_score(start=pointer, end=end)
                        )
                    )

                best = max(best, total)

            memo[start][end] = best
            return best


        return find_maximum_score(start=0, end=len(stoneValue))
```

- Time complexity is O(N^2).
- Space complexity is O(N^2).
