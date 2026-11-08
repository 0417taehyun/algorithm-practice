# 9. Palindrome Number

## Problem

- [9. Palindrome Number](https://leetcode.com/problems/palindrome-number)

## Solution

### 1. Convert into String

```Python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        num_str = str(x)
        start, end = 0, len(num_str)-1

        while start <= end:
            if num_str[start] != num_str[end]:
                return False

            start += 1
            end -= 1

        return True

```

- Time complexity is O(N).
- Space complexity is O(N).

### 2. Using Digits

```Python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        origin = x
        reversed_num = 0
        while x > 0:
            reversed_num = (reversed_num * 10) + (x % 10)
            x = x // 10

        return origin == reversed_num

```

- Time complexity is O(logN).
- Space complexity is O(1).
