# 1386. Cinema Seat Allocation

## Problem

- [1386. Cinema Seat Allocation](https://leetcode.com/problems/cinema-seat-allocation)

## Solution

### 1. Classification

> Memory Limit Exceeded

```Python
class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        left_candidates = set([2, 3, 4, 5])
        mid_candidates = set([4, 5, 6, 7])
        right_candidates = set([6, 7, 8, 9])

        rows = [{"left": 1, "mid": 1, "right": 1} for _ in range(n+1)]
        for row, seat in reservedSeats:
            if seat in left_candidates:
                rows[row]["left"] = 0
            if seat in mid_candidates:
                rows[row]["mid"] = 0
            if seat in right_candidates:
                rows[row]["right"] = 0

        answer = 0
        for row in rows[1:]:
            total = row["left"] + row["mid"] + row["right"]

            if row["left"] == 1 and row["mid"] == 1:
                total -= 1

            if row["left"] == 0 and row["mid"] == 1 and row["right"] == 1:
                total -= 1

            answer += total

        return answer
```

> N refers the number of rows.

- Time complexity is O(N).
- Space complexity is O(N).

### 2. Optimization

```Python
class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        left_candidates = set([2, 3, 4, 5])
        mid_candidates = set([4, 5, 6, 7])
        right_candidates = set([6, 7, 8, 9])

        # [{row: {"left": 0, "mid": 0, "right": 0}}]
        have_seats = {}
        for row, seat in reservedSeats:
            if row not in have_seats:
                have_seats[row] = {"left": 1, "mid": 1, "right": 1}

            if seat in left_candidates:
                have_seats[row]["left"] = 0

            if seat in mid_candidates:
                have_seats[row]["mid"] = 0

            if seat in right_candidates:
                have_seats[row]["right"] = 0

        answer = (n - len(have_seats)) * 2
        for row in have_seats.values():
            total = row["left"] + row["mid"] + row["right"]

            if row["mid"] == 1 and (row["left"] == 1 or row["right"] == 1):
                total -= 1

            answer += total

        return answer
```

> N refers the length of reservedSeats

- Time complexity is O(N).
- Space complexity is O(N).
