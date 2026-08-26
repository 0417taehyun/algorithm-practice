# 2904. Shortest and Lexicographically Smallest Beautiful String

## Problem

- [2904. Shortest and Lexicographically Smallest Beautiful String](https://leetcode.com/problems/shortest-and-lexicographically-smallest-beautiful-string)

## Solution

### 1. Brute Force

```Python
class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        indexes = []
        for idx, binary in enumerate(s):
            if binary == "1":
                indexes.append(idx)

        if len(indexes) < k:
            return ""

        candidates = []
        minimum_length = 101
        start = 0
        end = start + k - 1
        while end < len(indexes):
            if (indexes[end] - indexes[start] + 1) < minimum_length:
                candidates = [indexes[start:end+1]]
                minimum_length = indexes[end] - indexes[start] + 1
            elif (indexes[end] - indexes[start] + 1) == minimum_length:
                candidates.append(indexes[start:end+1])

            start += 1
            end = start + k - 1

        answer = "1" * minimum_length
        for candidate in candidates:
            base = ""
            candidate_set = set(candidate)
            for idx in range(candidate[0], candidate[-1]+1):
                if idx in candidate_set:
                    base += "1"
                else:
                    base += "0"

            answer = min(answer, base)

        return answer

```

- Time complexity is O(N^2).
- Space complexity is O(N).

### 2. Using Sliding Window

```Python
class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        if s.count("1") < k:
            return ""

        left = 0
        count = 0
        answer = s
        for right, binary in enumerate(s):
            count += int(binary)
            while count > k or s[left] == "0":
                count -= int(s[left])
                left += 1

            if count == k:
                current = s[left:right+1]
                if (
                    len(current) < len(answer)
                    or (
                        len(current) == len(answer)
                        and current < answer
                    )
                ):
                    answer = current

        return answer

```

- Time complexity is O(N^2).
- Space complexity is O(N).
