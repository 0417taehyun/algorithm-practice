# 3731. Find Missing Elements

## Problem

- [3731. Find Missing Elements](https://leetcode.com/problems/find-missing-elements)

## Solution

### 1. Brute Force

```Python
class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        candidates = [False] * 101
        smallest = 101
        largest = 0

        for num in nums:
            if num < smallest:
                smallest = num

            if num > largest:
                largest = num

            candidates[num] = True

        result = []
        for idx in range(smallest, largest+1):
            if not candidates[idx]:
                result.append(idx)

        return result

```

> Based on the constraints, the maximum number of nums[i] is 100 and the N below refers 101.

- Time complexity is O(N).
- Space complexity is O(N).
