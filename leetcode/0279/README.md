# 279. Perfect Squares

## Problem

- [279. Perfect Squares](https://leetcode.com/problems/perfect-squares)

## Solution

### 1. Depth-First Search (DFS) with Memoization

```Python
class Solution:
    def numSquares(self, n: int) -> int:
        memo = [0] * (n + 1)


        def dfs(num: int) -> int:
            if memo[num] != 0:
                return memo[num]

            if num < 4:
                memo[num] = num
                return num

            candidate = 1
            candidates = []
            while candidate**2 <= num:
                candidates.append(candidate**2)
                candidate += 1

            answer = 10**4
            for candidate in candidates[::-1]:
                count = dfs(num=num-candidate) + 1
                answer = min(answer, count)

            memo[num] = answer
            return answer


        return dfs(num=n)

```

- Time complexity is O(N\*logN).
- Space complexity is O(N).
