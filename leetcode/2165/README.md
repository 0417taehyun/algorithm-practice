# 2165. Smallest Value of the Rearranged Number

## Problem

- [2165. Smallest Value of the Rearranged Number](https://leetcode.com/problems/smallest-value-of-the-rearranged-number)

## Solution

### 1. Classification

```Python
class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return num

        counter = [0] * 10

        # If num > 0, we need to use minimum number.
        if num > 0:
            for digit in str(num):
                counter[int(digit)] += 1

            answer = ""
            for num, count in enumerate(counter):
                if count > 0 and num != 0:
                    answer += str(num)
                    counter[num] -= 1
                    break

            for num, count in enumerate(counter):
                answer += (str(num) * count)

            return int(answer)

        # If num < 0, we need to use maximum number.
        for digit in str(num)[1:]:
            counter[int(digit)] += 1

        answer = "-"
        for num in range(len(counter)-1, -1, -1):
            count = counter[num]
            if count > 0:
                answer += (str(num) * count)

        return int(answer)

```

> N refers the length of the input number and the maximum is 15.
> This is because the constraint, -10^15 <= num <= 10^15.
> Therefore, the time complexity is O(1).

- Time complexity is O(1).
- Space complexity is O(1).
