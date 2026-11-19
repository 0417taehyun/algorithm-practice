# 647. Palindromic Substrings

## Problem

- [647. Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings)

## Solution

### 1. Expand from Centers

```Python
class Solution:
    def countSubstrings(self, s: str) -> int:
        def count_palindrome(left: int, right: int) -> int:
            total = 0

            while left >= 0 and right < len(s) and s[left] == s[right]:
                total += 1
                left -= 1
                right += 1

            return total


        answer = 0
        for idx in range(len(s)):
            answer += count_palindrome(left=idx, right=idx)
            answer += count_palindrome(left=idx, right=idx+1)

        return answer

```

- Time complexity is O(N^2).
- Space complexity is O(1).
