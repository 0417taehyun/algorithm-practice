# 1477. Find Two Non-overlapping Sub-arrays Each With Target Sum

## Problem

- [1477. Find Two Non-overlapping Sub-arrays Each With Target Sum](https://leetcode.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum)

## Solution

### 1. Two Pointers with Prefix Sum

> The below solution is my intial attempt and it was a wrong answer

```Python
class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        memo = []
        count = 0
        left = 0
        right = 1

        prefix_sum = [0] * (len(arr) + 1)
        for idx in range(len(arr)):
            prefix_sum[idx+1] = arr[idx] + prefix_sum[idx]

        while left < len(prefix_sum) and right < len(prefix_sum):
            if prefix_sum[right] - prefix_sum[left] > target:
                left = right
                right = left + 1

            elif prefix_sum[right] - prefix_sum[left] < target:
                right += 1

            else:
                memo.append(right-left)
                left = right
                right = left + 1

        if len(memo) >= 2:
            memo.sort()
            return memo[0] + memo[1]

        return -1
```

- Time complexity is O(N\*logN).
- Space complexity is O(N).
