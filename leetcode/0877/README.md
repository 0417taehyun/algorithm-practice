# 877. Stone Game

## Problem

- [877. Stone Game](https://leetcode.com/problems/stone-game)

## Solution

### 1. Recursion

> Time Limit Exceeded

```Python
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        left = 0
        right = len(piles) - 1

        def get_maximum_difference(left: int, right: int, piles: List[int]) -> int:
            if left == right:
                return piles[left]

            left_stones = piles[left] - get_maximum_difference(left=left+1, right=right, piles=piles)
            right_stones = piles[right] - get_maximum_difference(left=left, right=right-1, piles=piles)

            return max(left_stones, right_stones)

        return get_maximum_difference(left=left, right=right, piles=piles) >= 0

```

- Time complexity is O(2^N).
- Space complexity is O(N).

### 2. Dynamic Programming

```Python
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        left = 0
        right = len(piles) - 1

        memo = [[0] * len(piles) for _ in piles]

        def get_maximum_difference(left: int, right: int, piles: List[int], memo: List[int][int]) -> int:
            if memo[left][right] != 0:
                return memo[left][right]

            if left == right:
                return piles[left]

            left_stones = piles[left] - get_maximum_difference(left=left+1, right=right, piles=piles, memo=memo)
            right_stones = piles[right] - get_maximum_difference(left=left, right=right-1, piles=piles, memo=memo)

            memo[left][right] = max(left_stones, right_stones)

            return memo[left][right]

        return get_maximum_difference(left=left, right=right, piles=piles, memo=memo) > 0

```

- Time complexity is O(N^2).
- Space complexity is O(N^2).

### 3. Mathematical Approach

> If the length of list is even and the total number of stones across all the piles is odd, the first player always wins the game.
> This is because sum(even_index_numbers) can be lager than sum(odd_index_numbers), vice versa, and the first player can take the larger.
> For example, if the first player take the even-index number first, then the second player can only choose odd-index number, and so on.

```Python
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return True

```

- Time complexity is O(1).
- Space complexity is O(1).
