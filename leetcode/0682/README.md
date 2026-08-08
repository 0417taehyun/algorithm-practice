# 682. Baseball Game

## Problem

- [682. Baseball Game](https://leetcode.com/problems/baseball-game)

## Solution

### 1. Using Stack

```Python
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        result = 0
        records = []

        for operation in operations:
            if operation == "+":
                second_score = records[-1]
                first_score = records[-2]
                new_score = first_score+second_score

                result += new_score
                records.append(new_score)

            elif operation == "C":
                prev_score = records.pop()
                result -= prev_score

            elif operation == "D":
                prev_score = records[-1]

                result += (prev_score * 2)
                records.append(prev_score*2)

            else:
                score = int(operation)

                result += score
                records.append(score)

        return result
```

- Time complexity is O(N).
- Space complexity is O(N).
