# 5. Longest Palindromic Substring

## Problem

- [5. Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)

## Solution

### 1. Expand from the center

```Python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def get_the_longest_palindrome(left: int, right: int) -> (str, int):
            word = ""
            length = 0

            # Expand from the center
            while left >= 0 and right < len(s) and s[left] == s[right]:
                word = s[left:right+1]
                length = right - left + 1

                left -= 1
                right += 1

            return word, length


        answer = ""
        max_length = 0
        for idx in range(len(s)):
            # Odd
            word, length = get_the_longest_palindrome(left=idx, right=idx)
            if length > max_length:
                answer = word
                max_length = length

            # Even
            word, length = get_the_longest_palindrome(left=idx, right=idx+1)
            if length > max_length:
                answer = word
                max_length = length

        return answer

```

- Time complexity is O(N^2).
- Space complexity is O(1).
