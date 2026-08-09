# 1441. Build an Array With Stack Operations

## Problem

- [1441. Build an Array With Stack Operations](https://leetcode.com/problems/build-an-array-with-stack-operations)

## Solution

### 1. Simulation

```Python
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        result = []

        target_idx = 0
        for number in range(1, n+1):
            if target[target_idx] == number:
                result.append("Push")
                target_idx += 1
            else:
                result.append("Push")
                result.append("Pop")

            if target_idx > len(target) - 1:
                break

        return result

```

- Time complexity is O(N).
- Space complexity is O(1).
