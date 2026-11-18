# 359. Logger Rate Limiter

## Problem

- [359. Logger Rate Limiter](https://leetcode.com/problems/logger-rate-limiter)

## Solution

### 1. Using Hash Map

```Python
class Logger:

    def __init__(self):
        # {"message": "available_timestamp": }
        self.logs = {}
        self.threathold = 10

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.logs:
            self.logs[message] = timestamp

        if self.logs[message] <= timestamp:
            self.logs[message] = timestamp + self.threathold
            return True

        return False


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
```

- Time complexity is O(1).
- Space complexity is O(N).
