# 1. Two Sum

## Problem

- [1. Two Sum](https://leetcode.com/problems/two-sum)

## Solution

### 1. Using Two Pointers with Sorted Array

```Python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # {num: [indexes]}
        origin_indexes = {}
        for idx, num in enumerate(nums):
            if not num in origin_indexes:
                origin_indexes[num] = []
            origin_indexes[num].append(idx)

        nums.sort()
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] + nums[right] == target:
                return [ origin_indexes[nums[left]].pop(), origin_indexes[nums[right]].pop() ]

            if nums[left] + nums[right] > target:
                right -= 1
            else:
                left += 1
```

- Time complexity is O(N\*logN).
- Space complexity is O(N).

### 2. Using Hash Map

```Python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # {number: index}
        numbers = {}
        for idx, number in enumerate(nums):
            diff = target - number
            if diff in numbers:
                return [idx, numbers[diff]]

            numbers[number] = idx

```

- Time complexity is O(N).
- Space complexity is O(N).
