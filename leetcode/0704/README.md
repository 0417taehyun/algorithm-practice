# 704. Binary Search

## Problem

- [704. Binary Search](https://leetcode.com/problems/binary-search)

## Solution

### 1. Using Binary Search

```Python
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums)-1

        while left <= right:
            mid = (left + right) // 2

            if target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
            else:
                return mid

        return -1

```

- Time complexity is O(logN).
- Space complexity is O(1).
