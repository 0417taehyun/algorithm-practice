# 541. Reverse String II

## Problem

- [541. Reverse String II](https://leetcode.com/problems/reverse-string-ii)

## Solution

### 1. Simulation

```Python
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        answer = list(s)
        for idx in range(0, len(s), 2*k):
            answer[idx:idx+k] = reversed(answer[idx:idx+k])

        return "".join(answer)

```

- Time complexity is O(N).
- Space complexity is O(N).
