# 88. Merge Sorted Array

## Problem

- [88. Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array)

## Solution

### 1. Three Pointers

```Python
class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        left, right = m-1, n-1
        for idx in range(m+n-1, -1, -1):
            if right < 0:
                break

            if left >= 0 and nums1[left] > nums2[right]:
                nums1[idx] = nums1[left]
                left -= 1
            else:
                nums1[idx] = nums2[right]
                right -= 1

```

- Time complexity is O(M+N).
- Space complexity is O(1).
