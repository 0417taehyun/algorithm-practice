# 1510. Stone Game IV

## Problem

- [1510. Stone Game IV](https://leetcode.com/problems/stone-game-iv)

## Solution

### 1. Top-Down Dynamic Programming (Memoization)

```Python
class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        # List of square number candidates
        candidate = 1
        candidates = []
        while candidate ** 2 <= n:
            candidates.append(candidate**2)
            candidate += 1


        # Memorize each remained stones optimal result.
        memo = [None] * (n + 1)


        def dfs(remaining: int) -> bool:
            if memo[remaining] is not None:
                return memo[remaining]

            # If the number of remained stones is zero, the current player loses the game.
            if remaining == 0:
                memo[remaining] = False
                return False

            # If the number of remained stones is a square number, the current plyaer wins the game.
            # This is becaus each player plays optimally and they choose the square number to win the game.
            if remaining in candidates:
                memo[remaining] = True
                return True

            for candidate in candidates:
                if candidate > remaining:
                    break

                # If the next player has no chances to win, the current player wins the game.
                if not dfs(remaining=remaining-candidate):
                    memo[remaining] = True
                    return True

            # There are no ways to win the game.
            memo[remaining] = False
            return False


        return dfs(remaining=n)

```

- Time complexity is O(N\*sqrt(N)).
- Space complexity is O(N).
