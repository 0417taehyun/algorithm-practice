# 448. Find All Numbers Disappeared in an Array

## Problem

- [448. Find All Numbers Disappeared in an Array](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array)

## Solution

### 1. Brute Force

```Python
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        count = [0] * len(nums)

        for num in nums:
            count[num-1] += 1

        return [ num+1 for num, cnt in enumerate(count) if cnt == 0 ]
```

- Time complexity is O(N).
- Space complexity is O(N).

### 2. Cycle Sort

```Python
class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        answer = []

        idx = 0
        while idx < len(nums):
            correct = nums[idx] - 1
            if (
                idx == correct
                or nums[idx] == nums[correct]
            ):
                idx += 1
            else:
                nums[idx], nums[correct] = nums[correct], nums[idx]

        for idx, num in enumerate(nums):
            if (num - 1) != idx:
                answer.append(idx + 1)

        return answer

```

- Time complexity is O(N).
- Space complexity is O(1).
