# 3718. Smallest Missing Multiple of K

## Problem

- [3718. Smallest Missing Multiple of K](https://leetcode.com/problems/smallest-missing-multiple-of-k)

## Solution

### 1. Using Predefined Array

```Python
class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        numbers = [0] * 201
        for num in nums:
            numbers[num] += 1

        for num in range(k, 201, k):
            if numbers[num] == 0:
                return num

```

- Time complexity is O(N).
- Space complexity is O(N).

### 2. Using Hash Table

```Python
class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        answer = k
        seen = set(nums)
        while answer in seen:
            answer += k
        return answer

```

- Time complexity is O(N).
- Space complexity is O(N).
