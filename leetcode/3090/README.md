# 3090. Maximum Length Substring With Two Occurrences

## Problem

- [3090. Maximum Length Substring With Two Occurrences](https://leetcode.com/problems/maximum-length-substring-with-two-occurrences)

## Solution

### 1. Brute Force

```Python
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        max_length = 0
        for start in range(len(s)):
            end = start
            occurency = {}
            while end < len(s):
                end_character = s[end]
                if end_character in occurency:
                    occurency[end_character] += 1
                else:
                    occurency[end_character] = 1

                if occurency[end_character] == 3:
                    break

                end += 1

            max_length = max(max_length, end-start)

        return max_length
```

- Time complexity is O(N^2).
- Space complexity is O(N).

### 2. Sliding Window

```Python
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        max_length = 0
        start_idx = 0
        occurency = {}
        for end_idx, end_character in enumerate(s):
            if end_character in occurency:
                occurency[end_character] += 1
            else:
                occurency[end_character] = 1

            while occurency[end_character] > 2:
                start_character = s[start_idx]
                occurency[start_character] -= 1
                start_idx += 1

            max_length = max(max_length, end_idx-start_idx+1)

        return max_length
```

- Time complexity is O(N).
- Space complexity is O(N).
