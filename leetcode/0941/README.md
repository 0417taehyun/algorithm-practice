# 941. Valid Mountain Array

## Problem

- [941. Valid Mountain Array](https://leetcode.com/problems/valid-mountain-array)

## Solution

### 1. Using Two Pointers

```Python
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        if n < 3:
            return False

        left = 0
        while left < (len(arr) - 1) and arr[left] < arr[left+1]:
            if arr[left] == arr[left+1]:
                return False
            left += 1

        right = n - 1
        while right >= 0 and arr[right] < arr[right-1]:
            if arr[right] == arr[right-1]:
                return False
            right -= 1

        # Peak can't be first or last
        if left == 0 or right == (n - 1):
            return False

        return left == right

```

- Time complexity is O(N).
- Space complexity is O(1).
