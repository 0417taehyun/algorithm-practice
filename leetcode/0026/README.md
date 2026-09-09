# 26. Remove Duplicates from Sorted Array

## Problem

- [26. Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array)

## Solution

### 1. Two Pointers

```Python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        insert_idx = 1
        for idx in range(1, len(nums)):
            if nums[idx] != nums[idx-1]:
                nums[insert_idx] = nums[idx]
                insert_idx += 1

        return insert_idx

```

- Time complexity is O(N).
- Space complexity is O(1).

### 2. Optimize Operation

> Swap when it really needs

```Python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        answer = 1
        left, right = 0, 1
        while right < len(nums):
            if nums[left] == nums[right]:
                right += 1

            else:
                if (right - left) > 1:
                    nums[left+1], nums[right] = nums[right], nums[left+1]

                left += 1
                right += 1
                answer += 1

        return answer
```

- Time complexity is O(N).
- Space complexity is O(1).
