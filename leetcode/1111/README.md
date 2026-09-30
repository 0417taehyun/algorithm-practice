# 1111. Maximum Nesting Depth of Two Valid Parentheses Strings

## Problem

- [1111. Maximum Nesting Depth of Two Valid Parentheses Strings](https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings)

## Solution

### 1. Split

```Python
class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        prev = ""
        answer = []
        subsequence = 0
        for character in seq:
            if character == "(":
                if prev == "(":
                    subsequence = (subsequence + 1) % 2

                answer.append(subsequence)

            else:
                if prev == ")":
                    subsequence = (subsequence + 1) % 2

                answer.append(subsequence)

            prev = character

        return answer

```

- Time complexity is O(N).
- Space complexity is O(1).
