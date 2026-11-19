# 409. Longest Palindrome

## Problem

- [409. Longest Palindrome](https://leetcode.com/problems/longest-palindrome)

## Solution

### 1. Using Hash Map

```Python
class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = {}
        for character in s:
            counter[character] = counter.get(character, 0) + 1

        answer = 0
        has_odd = False
        for count in counter.values():
            if count % 2 == 0:
                answer += count
            else:
                has_odd = True
                answer += (count - 1)

        if has_odd:
            answer += 1

        return answer

```

> We only manage 52 characters (lower and upper English letters), which measn the space complexity is constant.

- Time complexity is O(N).
- Space complexity is O(1).
