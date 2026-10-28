# 859. Buddy Strings

## Problem

- [859. Buddy Strings](https://leetcode.com/problems/buddy-strings)

## Solution

### 1. Case Analysis

```Python
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) == 1 or len(goal) == 1:
            return False

        if len(s) != len(goal):
            return False

        unmatched_cnt = 0
        s_diff, g_diff = set(), set()

        for s_character, g_character in zip(s, goal):
            if s_character != g_character:
                unmatched_cnt += 1
                s_diff.add(s_character)
                g_diff.add(g_character)

            if unmatched_cnt > 2:
                return False

        if unmatched_cnt == 1:
            return False

        if unmatched_cnt == 0:
            return len(set(s)) != len(s)

        return s_diff == g_diff

```

> The maximum number of set is 26, constant.

- Time complexity is O(N).
- Space complexity is O(1).
