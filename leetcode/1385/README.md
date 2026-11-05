# 1385. Find the Distance Value Between Two Arrays

## Problem

- [1385. Find the Distance Value Between Two Arrays](https://leetcode.com/problems/find-the-distance-value-between-two-arrays)

## Solution

### 1. Brute Force

```Python
class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        answer = 0
        for arr1_num in arr1:
            is_distance_value = True
            for arr2_num in arr2:
                if abs(arr1_num - arr2_num) <= d:
                    is_distance_value = False

            if is_distance_value:
                answer += 1

        return answer

```

- Time complexity is O(N^2).
- Space complexity is O(1).
