# 58. Length of Last Word

## Problem

- [58. Length of Last Word](https://leetcode.com/problems/length-of-last-word)

## Solution

### 1. Case Analysis

```Python
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        prev_char = ""
        prev, curr = 0, 0
        for character in s:
            if character == " ":
                if prev_char != " ":
                    prev = curr
                curr = 0
            else:
                curr += 1

            prev_char = character

        if curr == 0:
            return prev

        return curr

```

- Time complexity is O(N).
- Space complexity is O(1).
