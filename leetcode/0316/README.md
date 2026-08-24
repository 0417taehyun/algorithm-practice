# 316. Remove Duplicate Letters

## Problem

- [316. Remove Duplicate Letters](https://leetcode.com/problems/remove-duplicate-letters)

## Solution

### 1. Using Stack

```Python
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # {character}
        visited = set()

        # [character]
        stack = []

        last_positions = {character: idx for idx, character in enumerate(s)}

        for idx, character in enumerate(s):
            if character not in visited:
                while (
                    stack
                    and stack[-1] > character
                    and last_positions[stack[-1]] > idx
                ):
                    top = stack.pop()
                    visited.discard(top)

                stack.append(character)
                visited.add(character)

        return "".join(stack)
```

> N refers the length of the input `s`.
> Since we only use lower case English letters, the space complexity is O(1).

- Time complexity is O(N).
- Space complexity is O(1).
