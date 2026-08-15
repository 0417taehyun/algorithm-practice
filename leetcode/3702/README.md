# 3702. Longest Subsequence With Non-Zero Bitwise XOR

## Problem

- [3702. Longest Subsequence With Non-Zero Bitwise XOR](https://leetcode.com/problems/longest-subsequence-with-non-zero-bitwise-xor)

## Solution

### 1. Classification with XOR Properties

```Python
class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        total_xor = 0
        is_all_zero = True

        for num in nums:
            if num != 0:
                is_all_zero = False

            total_xor ^= num

        if total_xor != 0:
            return len(nums)

        # `sub` means removing x from the total
        # x XOR sub = 0 -> x XOR x XOR sub = x XOR 0 -> 0 XOR sub = x -> sub = x
        # Therefore, if we only remove x, we can get non-zero XOR result
        if not is_all_zero:
            return len(nums) - 1

        return 0

```

- Time complexity is O(N).
- Space complexity is O(1).
