# 27. Remove Element

## Problem

- [27. Remove Element](https://leetcode.com/problems/remove-element)

## Solution

### 1. Two Pointers

```Python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for idx in range(len(nums)):
            if nums[idx] != val:
                nums[k] = nums[idx]
                k += 1

        return k

```

- Time complexity is O(N).
- Space complexity is O(1).

### 2. Two Pointers, Optimizaing the worst case

```Python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        start = 0
        end = len(nums)

        while start < end:
            if nums[start] == val:
                end -= 1
                nums[start] = nums[end]
            else:
                start += 1

        return end

```

> The solution above only replaces when it should be.

- Time complexity is O(N).
- Space complexity is O(1).
