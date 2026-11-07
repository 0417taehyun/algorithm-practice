# 2810. Faulty Keyboard

## Problem

- [2810. Faulty Keyboard](https://leetcode.com/problems/faulty-keyboard)

## Solution

### 1. Simulation

```Python
class Solution:
    def finalString(self, s: str) -> str:
        answer = []
        for character in s:
            if character == "i":
                answer = answer[::-1]
            else:
                answer.append(character)

        return "".join(answer)

```

- Time complexity is O(N).
- Space complexity is O(N).
