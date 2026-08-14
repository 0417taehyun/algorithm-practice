# 125. Valid Palindrome

## Problem

- [125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome)

## Solution

### 1. Using Two Pointers

```Python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1

        while start < end:
            while start < end and not s[start].isalnum():
                start += 1

            while start < end and not s[end].isalnum():
                end -= 1

            if s[start].lower() != s[end].lower():
                return False

            start += 1
            end -= 1

        return True

```

- Time complexity is O(N).
- Space complexity is O(1).
