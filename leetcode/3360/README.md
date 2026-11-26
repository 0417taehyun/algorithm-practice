# 3360. Stone Removal Game

## Problem

- [3360. Stone Removal Game](https://leetcode.com/problems/stone-removal-game)

## Solution

### 1. Simulation

```Python
class Solution:
    def canAliceWin(self, n: int) -> bool:
        cases = []
        start = 10
        is_alice_win = False
        while start > 0:
            if start % 2 == 0:
                is_alice_win = False
            else:
                is_alice_win = True

            if not cases:
                cases.append((start, is_alice_win))
            else:
                cases.append((cases[-1][0]+start, is_alice_win))

            start -= 1

        for case, is_alice_win in cases:
            if n < case:
                return is_alice_win

```

- Time complexity is O(1).
- Space complexity is O(1).
