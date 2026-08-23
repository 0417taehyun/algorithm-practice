# 1927. Sum Game

## Problem

- [1927. Sum Game](https://leetcode.com/problems/sum-game)

## Solution

### 1. Classification

```Python
class Solution:
    def sumGame(self, num: str) -> bool:
        left, right = 0, len(num)-1
        left_sum, right_sum, left_cnt, right_cnt = 0, 0, 0, 0
        while left < right:
            if num[left] == '?':
                left_cnt += 1
            elif num[left] != '?':
                left_sum += int(num[left])

            if num[right] == '?':
                right_cnt += 1
            elif num[right] != '?':
                right_sum += int(num[right])

            left += 1
            right -= 1

        if (left_cnt + right_cnt) == 0 and left_sum != right_sum:
            return True

        # Alice always win if the number of total question marks is odd.
        if (left_cnt + right_cnt) % 2 == 1:
            return True

        # If Bob wans to set (Alice + Bob) = S to win the game, Bob = (S - Alice).
        # Bob can choose between 0 and 9, thus 0 <= S - Alice <= 9.
        # Alice also can choose between 0 and 9, thus 0 <= S <= 9 or 9 <= S <= 18.
        # Therefore, if Bob wants to win, S should be 9 because 9 is the only number can cover the case.
        #
        # [A, B, A, B, A, B, ...] -> A refers Alice, B refers Bob
        # [1, 8, 5, 4, 9, 0, ...]
        # Consequently, (Sum(Alice) + Sum(Bob)) should be 9n.
        #
        # However, since both Alice and Bob play the game, we need to doulbe the case.
        # Consequently, S * 2 = question_marks * 9
        # (left_sum - right_sum) refers S, and (richt_cnt - left_cnt) refers question_marks.
        return (left_sum - right_sum) * 2 != (right_cnt - left_cnt) * 9

```

- Time complexity is O(N).
- Space complexity is O(1).
