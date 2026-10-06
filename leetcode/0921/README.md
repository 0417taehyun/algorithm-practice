# 921. Minimum Add to Make Parentheses Valid

## Problem

- [921. Minimum Add to Make Parentheses Valid](https://leetcode.com/problems/minimum-add-to-make-parentheses-valid)

## Solution

### 1. Count

```Python
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        answer = 0
        open_cnt = 0

        for character in s:
            if character == "(":
                open_cnt += 1
            else:
                if open_cnt == 0:
                    answer += 1
                else:
                    open_cnt -= 1
        return answer + open_cnt
```

- Time complexity is O(N).
- Space complexity is O(1).
