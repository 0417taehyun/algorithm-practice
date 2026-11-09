# 646. Maximum Length of Pair Chain

## Problem

- [646. Maximum Length of Pair Chain](https://leetcode.com/problems/maximum-length-of-pair-chain)

## Solution

### 1. Using Sort with Greedy

```Python
class Solution:
    def findLongestChain(self, pairs: list[list[int]]) -> int:
        pairs.sort(key=lambda x: x[1])

        curr = -1001
        answer = 0
        for start, end in pairs:
            if start > curr:
                answer += 1
                curr = end

        return answer

```

- Time complexity is O(N\*logN).
- Space complexity is O(N).
