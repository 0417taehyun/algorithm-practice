# 1524. Number of Sub-arrays With Odd Sum

## Problem

- [1524. Number of Sub-arrays With Odd Sum](https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum)

## Solution

### 1. Dynamic Programming

```Python
class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        odd, even, answer = 0, 0, 0
        for num in arr:
            # odd+even or even+even => both are even
            if num % 2 == 0:
                # +1 means, need single even subarray
                even += 1
            # odd+odd or even+odd => turn over
            else:
                # +1 means, need single odd subarray
                odd, even = even+1, odd

            answer = (answer + odd) % (10**9 + 7)

        return answer

```

- Time complexity is O(N).
- Space complexity is O(1).
