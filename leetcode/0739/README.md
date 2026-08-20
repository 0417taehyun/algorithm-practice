# 739. Daily Temperatures

## Problem

- [739. Daily Temperatures](https://leetcode.com/problems/daily-temperatures)

## Solution

### 1. Using Stack

```Python
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        answer[-1] = 0

        # [(temperature, index)]
        stack = [(temperatures[-1], len(temperatures)-1)]
        for idx in range(len(temperatures)-2, -1, -1):
            while stack and stack[-1][0] <= temperatures[idx]:
                stack.pop()

            if not stack:
                answer[idx] = 0
            else:
                answer[idx] = stack[-1][1] - idx

            stack.append((temperatures[idx], idx))

        return answer

```

- Time complexity is O(N).
- Space complexity is O(N).

### 2. Space Optimization

```Python
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)

        hottest = 0
        for idx in range(len(temperatures)-1, -1, -1):
            if temperatures[idx] >= hottest:
                hottest = temperatures[idx]
                continue

            days = 1
            while temperatures[idx] >= temperatures[idx+days]:
                days += answer[idx+days]

            answer[idx] = days

        return answer

```

- Time complexity is O(N).
- Space complexity is O(1).
