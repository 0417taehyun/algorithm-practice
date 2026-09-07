# 940. Distinct Subsequences II

## Problem

- [940. Distinct Subsequences II](https://leetcode.com/problems/distinct-subsequences-ii)

## Solution

### 1. Dynamic Programming

```Python
class Solution:
    def distinctSubseqII(self, s: str) -> int:
        dp = [1]

        # {alphabe: indx}
        last_index = {}

        # If the length of string `s` is N, the non-empty subsequences of s will be (2^N - 1).
        # Therefore, if a new alphabet appended to the string `s`, the number of subsequences will be doulbed.
        # We use Dynamic Programming, which looks like dp[i] = dp[i-1] * 2.
        for idx, alphabet in enumerate(s):

            # A new alphabet appended to the string
            dp.append(dp[-1] * 2)

            # Remove duplication
            #
            # For example,
            # [a, b, c, d, e, f, d]
            #
            # The below two cases are duplicated.
            # [a, b, c, d, ., ., .]
            # [a, b, c, ., ., ., d]
            #
            # Therefore, if the current index of `d` is I and the last index of `d` is J,
            # dp[I] = (dp[I-1] * 2) - dp[J-1].
            if alphabet in last_index:
                dp[-1] -= dp[last_index[alphabet]]

            last_index[alphabet] = idx

        return (dp[-1] - 1) % (10**9 + 7)
```

- Time complexity is O(N).
- Space complexity is O(N).

### 2. Space Optimization

```Python
class Solution:
    def distinctSubseqII(self, s: str) -> int:
        prev, curr = 1, 1
        last_count = {}

        for alphabet in s:
            curr = prev * 2
            if alphabet in last_count:
                curr -= last_count[alphabet]

            last_count[alphabet] = prev
            prev = curr

        return (curr - 1) % (10**9 + 7)
```

> Since we only create a fixed number of `last_count` dictionary, the space complexity is O(1).

- Time complexity is O(N).
- Space complexity is O(1).
