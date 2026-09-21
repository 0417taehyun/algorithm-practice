# 3524. Find X Value of Array I

## Problem

- [3524. Find X Value of Array I](https://leetcode.com/problems/find-x-value-of-array-i)

## Solution

### 1. Dynamic Programming

```Python
class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        answer = [0] * k
        prev = [0] * k

        for num in nums:
            curr = [0] * k
            curr[num % k] += 1
            for remainder in range(k):
                # Update
                curr[(remainder * num) % k] += prev[remainder]

            prev = curr
            for remainder in range(k):
                answer[remainder] += prev[remainder]

        return answer

```

> Due to constraints, 1 <= k <= 5, k is a constant.

- Time complexity is O(N).
- Space complexity is O(N).
