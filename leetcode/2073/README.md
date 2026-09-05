# 2073. Time Needed to Buy Tickets

## Problem

- [2073. Time Needed to Buy Tickets](https://leetcode.com/problems/time-needed-to-buy-tickets)

## Solution

### 1. Using One Pass

```Python
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        answer = 0
        for idx, ticket in enumerate(tickets):
            if idx <= k:
                answer += min(ticket, tickets[k])
            else:
                answer += min(ticket, tickets[k]-1)

        return answer

```

- Time complexity is O(N).
- Space complexity is O(1).
