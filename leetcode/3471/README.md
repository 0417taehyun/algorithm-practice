# 3471. Find the Largest Almost Missing Integer

## Problem

- [3471. Find the Largest Almost Missing Integer](https://leetcode.com/problems/find-the-largest-almost-missing-integer)

## Solution

### 1. Brute Force

```Python
class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        # {number: count}
        counter = {}

        start = 0
        while (start + k) <= len(nums):
            for num in set(nums[start:start+k]):
                if not num in counter:
                    counter[num] = 0
                counter[num] += 1

            start += 1

        answer = -1
        for num, cnt in counter.items():
            if cnt == 1:
                answer = max(answer, num)

        return answer

```

- Time complexity is O(N^2).
- Space complexity is O(N).

### 2. Classification

```Python
class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)

        if (k == n):
            return max(nums)

        # {num: count}
        counter = {}
        for num in nums:
            if not num in counter:
                counter[num] = 0
            counter[num] += 1

        if (k == 1):
            answer = -1
            for num, cnt in counter.items():
                if cnt == 1:
                    answer = max(answer, num)
            return answer

        # 1 < k < n
        answer = -1

        start = nums[0]
        if counter[start] == 1:
            answer = max(answer, start)

        end = nums[-1]
        if counter[end] == 1:
            answer = max(answer, end)

        return answer
```

- Time complexity is O(N).
- Space complexity is O(N).
