# 2958. Length of Longest Subarray With at Most K Frequency

## Problem

- [2958. Length of Longest Subarray With at Most K Frequency](https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency)

## Solution

### 1. Top-Down Dynamic Programming (Memoization)

> Time and Memory Limit Exceeded

```Python
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        memo = [ [None] * (len(nums) + 1) for _ in range(len(nums) + 1) ]


        def dfs(start: int, end: int) -> int:
            if memo[start][end] is not None:
                return sum(memo[start][end].values())

            curr_length = 0
            temp = {}
            for num in nums[start:end+1]:
                if num in temp:
                    if temp[num] + 1 > k:
                        break

                    temp[num] += 1
                else:
                    temp[num] = 1

                curr_length += 1

            memo[start][end] = temp

            first_length = 0
            second_length = 0

            if end + 1 < len(nums):
                first_length = dfs(start=start, end=end+1)
                second_length = dfs(start=start+1, end=end+1)

            return max(curr_length, first_length, second_length)

        return dfs(start=0, end=0)

```

- Time complexity is O(N^2).
- Space complexity is O(N^2).

### 2. Sliding Window

```Python
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        max_length = 0

        start = 0
        frequency = {}
        for end in range(len(nums)):
            num = nums[end]
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1

            # If the frequency of the num is greater than k,
            # we need to decrease the size of subarray until the frequency is less than or equal to k.
            while k < frequency[num]:
                frequency[nums[start]] -= 1
                start += 1

            # Include start element
            max_length = max(max_length, end-start+1)

        return max_length

```

- Time complexity is O(N).
- Space complexity is O(N).
