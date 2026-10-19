# 2089. Find Target Indices After Sorting Array

## Problem

- [2089. Find Target Indices After Sorting Array](https://leetcode.com/problems/find-target-indices-after-sorting-array)

## Solution

### 1. Count Sort

```Python
class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        numbers = [0] * (target + 1)
        for number in nums:
            if number <= target:
                numbers[number] += 1

        if numbers[target] == 0:
            return []
        prev = sum(numbers[:target])
        return [ count + prev for count in range(numbers[target]) ]

```

- Time complexity is O(N).
- Space complexity is O(N).

### 2. Count Sort with Space Optimization

```Python
class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        prev = 0
        target_cnt = 0

        for number in nums:
            if number < target:
                prev += 1
            elif number == target:
                target_cnt += 1

        return [ prev + count for count in range(target_cnt) ]

```

- Time complexity is O(N).
- Space complexity is O(1).
