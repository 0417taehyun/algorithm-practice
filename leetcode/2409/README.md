# 2409. Count Days Spent Together

## Problem

- [2409. Count Days Spent Together](https://leetcode.com/problems/count-days-spent-together)

## Solution

### 1. Case Analysis

```Python
class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        def convert_to_int(date_string: str) -> List[int]:
            return [int(date) for date in date_string.split("-")]

        number_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        alice_arrive = convert_to_int(date_string=arriveAlice)
        alice_leave = convert_to_int(date_string=leaveAlice)
        bob_arrive = convert_to_int(date_string=arriveBob)
        bob_leave = convert_to_int(date_string=leaveBob)

        if (
            alice_leave[0] < bob_arrive[0]
            or (
                alice_leave[0] == bob_arrive[0]
                and alice_leave[1] < bob_arrive[1]
            )
        ):
            return 0

        if (
            bob_leave[0] < alice_arrive[0]
            or (
                bob_leave[0] == alice_arrive[0]
                and bob_leave[1] < alice_arrive[1]
            )
        ):
            return 0

        max_arrive = alice_arrive
        if (
            alice_arrive[0] < bob_arrive[0]
            or (
                alice_arrive[0] == bob_arrive[0]
                and alice_arrive[1] < bob_arrive[1]
            )
        ):
            max_arrive = bob_arrive

        min_leave = alice_leave
        if (
            alice_leave[0] > bob_leave[0]
            or (
                alice_leave[0] == bob_leave[0]
                and alice_leave[1] > bob_leave[1]
            )
        ):
            min_leave = bob_leave

        if max_arrive[0] == min_leave[0]:
            return min_leave[1] - max_arrive[1] + 1

        days = min_leave[1]
        for between_month in range(min_leave[0]-1, max_arrive[0], -1):
            days += number_of_days[between_month]

        days += (number_of_days[max_arrive[0]] - max_arrive[1] + 1)
        return days

```

- Time complexity is O(1).
- Space complexity is O(1).

### 2. Using Prefix Sum

```Python
class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        prefix_sum = [0]
        for idx, day in enumerate(days):
            prefix_sum.append(prefix_sum[idx] + day)


        def calculate_days(date: str) -> int:
            month, day = date.split("-")
            return prefix_sum[int(month)-1] + int(day)


        alice_arrive = calculate_days(date=arriveAlice)
        alice_leave = calculate_days(date=leaveAlice)
        bob_arrive = calculate_days(date=arriveBob)
        bob_leave = calculate_days(date=leaveBob)

        return max(
            0,
            min(alice_leave, bob_leave)
            - max(alice_arrive, bob_arrive)
            + 1
        )

```

- Time complexity is O(1).
- Space complexity is O(1).
