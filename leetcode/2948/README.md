# 2948. Make Lexicographically Smallest Array by Swapping Elements

## Problem

- [2948. Make Lexicographically Smallest Array by Swapping Elements](https://leetcode.com/problems/make-lexicographically-smallest-array-by-swapping-elements)

## Solution

### 1. Sorting and Using Hash Map

```Python
class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        # If |nums[i] - nums[j]| <= limit, locates in the same group.
        groups = []
        # {num: groups_index}
        group_map = {}

        for num in sorted(nums):
            # Add new group because [nums[i] - nums[j]] > limit
            if not groups or (num - groups[-1][-1]) > limit:
                groups.append([])
            groups[-1].append(num)
            group_map[num] = len(groups) - 1

        # Each group index
        group_idx = [0] * len(groups)
        for idx in range(len(nums)):
            group = group_map[nums[idx]]

            # Swap with the current smallest number in the group.
            nums[idx] = groups[group][group_idx[group]]
            group_idx[group] += 1

        return nums

```

- Time complexity is O(N\*logN).
- Space complexity is O(N).
