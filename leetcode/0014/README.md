# 14. Longest Common Prefix

## Problem

- [14. Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix)

## Solution

### 1. Simulation

```Python
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        answer = []
        for i in range(len(strs[0])):
            curr = strs[0][i]
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or curr != strs[j][i]:
                    return "".join(answer)

            answer.append(curr)

        return "".join(answer)

```

- Time complexity is O(N^2).
- Space complexity is O(1).
