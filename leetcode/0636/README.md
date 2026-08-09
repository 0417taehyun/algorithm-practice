# 636. Exclusive Time of Functions

## Problem

- [636. Exclusive Time of Functions](https://leetcode.com/problems/exclusive-time-of-functions)

## Solution

### 1. Using Stack

```Python
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        result = [0] * n

        stack = []
        prev_timestamp = 0
        for log in logs:
            function_id, operation, timestamp = log.split(":")
            function_id = int(function_id)
            timestamp = int(timestamp)

            if operation == "start":
                if stack:
                    prev_function_id = stack[-1]
                    result[prev_function_id] += (timestamp - prev_timestamp)

                stack.append(function_id)
                prev_timestamp = timestamp

            else:
                prev_function_id = stack.pop()
                result[prev_function_id] += (timestamp - prev_timestamp + 1)

                prev_timestamp = timestamp + 1

        return result

```

- Time complexity is O(N).
- Space complexity is O(N).
