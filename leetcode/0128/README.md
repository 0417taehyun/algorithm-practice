# 128. Longest Consecutive Sequence

## Problem

- [128. Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence)

## Solution

### 1. Using Set

```Python
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        answer, current_length = 0, 0
        num_set = set(nums)
        for num in num_set:
            if (num - 1) in num_set:
                continue

            current_length = 1
            curr = num
            while (curr + 1) in num_set:
                curr += 1
                current_length += 1

            answer = max(answer, current_length)

        return answer
```

- Time complexity is O(N).
- Space complexity is O(N).
