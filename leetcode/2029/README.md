# 2029. Stone Game IX

## Problem

- [2029. Stone Game IX](https://leetcode.com/problems/stone-game-ix)

## Solution

### 1. Using Remainders

```Python
class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        """
        Think about remainders for each value.
        - ex. [ 5, 4 ,3 ] => [ 2, 1, 0 ]

        There are only two ways Alice and Bob pick stones opimally if we ignore remainder 0.
        - [ A, B, A, B, A, B, ... ]
        - [ 1, 1, 2, 1, 2, 1, ... ] => If Alice starts with remainder 1, Bob always pick remainder 1
        - [ 2, 2, 1, 2, 1, 2, ... ] => If Alice starts with remainder 2, Bob always pick remainder 2

        Remainder 0 means Alice and Bob can switch their turns.
        Therefore, if the the number of remainder 0 is even, it does not affect the result.

        However, if the number of remainder 0 is odd,

        """
        # {remainder: count}
        counter = {0: 0, 1: 0, 2: 0}
        for stone in stones:
            counter[stone % 3] += 1

        # Remainder 0 does not affect each other because both Alice and Bob switch their turns.
        # Therefore, we only consider remainder 1 and 2.
        if counter[0] % 2 == 0:
            """
            If count(remainder 1) > 0 and count(remainder 2) >= count(remainder 1),
            Alice can start with remainder 1 and Bob should pick remainder 2 if there is no remainder 1.
            Therefore, Alice always win the game

            If counter(remainder 2) > 0 and counter(remainder 1) >= counter(remainder 2),
            Alice can start with remainder 2 and Bob should pick remainder 1 if there is not remainder 2.
            Therefore Alice Always win the game.

            Consequently, if count(remainder 1) > 0 and counter(remainder 2) > 0,
            Alice can start the less one, and always win the game.
            """
            return counter[1] > 0 and counter[2] > 0

        # Alice starts with the more one.
        # Alice needs start remainder, last remainder for Alice, and last remainder for Bob to win the game.
        # Therefore, if (remainder 1 >= remainder2 + 3 ) or (remainder 2 >= remainder1 + 3), Alice always win the game.
        return counter[1] - counter[2] >= 3 or counter[2] - counter[1] >= 3

```

- Time complexity is O(N).
- Space complexity is O(1).
