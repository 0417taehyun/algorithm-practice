# 287. Find the Duplicate Number

## Problem

- [287. Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number)

## Solution

### 1. Floyd's Tortoise and Hare with Cycle Sort

```Python
class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        slow, fast = nums[0], nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        fast = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return fast

```

- Time complexity is O(N).
- Space complexity is O(1).
