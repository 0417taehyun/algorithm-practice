# 3498. Reverse Degree of a String

## Problem

- [3498. Reverse Degree of a String](https://leetcode.com/problems/reverse-degree-of-a-string)

## Solution

### 1. Enumeration

```Python
class Solution:
    def reverseDegree(self, s: str) -> int:
        answer = 0
        for idx, alphabet in enumerate(s, start=1):
            answer += ((ord('z') - ord(alphabet) + 1) * idx)
        return answer

```

- Time complexity is O(N).
- Space complexity is O(1).
