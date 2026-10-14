# 3723. Maximize Sum of Squares of Digits

## Problem

- [3723. Maximize Sum of Squares of Digits](https://leetcode.com/problems/maximize-sum-of-squares-of-digits)

## Solution

### 1. Greedy

```Python
class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if (num * 9) < sum:
            return ""

        answer = []
        while num > 0:
            if sum >= 10:
                answer.append("9")
                sum -= 9
            else:
                answer.append(str(sum))
                sum -= sum
            num -= 1

        return "".join(answer)

```

> N refers num

- Time complexity is O(N).
- Space complexity is O(N).

### 2. Greedy (Optimization)

```Python
class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if (num * 9) < sum:
            return ""

        answer = []
        nine_count, remaining = divmod(sum, 9)
        answer.append((nine_count * "9"))
        if (num - nine_count) > 0:
            answer.append(str(remaining))
        answer.append((num - nine_count - 1) * "0")

        return "".join(answer)

```

> N refers num

- Time complexity is O(N).
- Space complexity is O(N).
