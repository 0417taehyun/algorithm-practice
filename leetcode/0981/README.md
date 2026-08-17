# 981. Time Based Key-Value Store

## Problem

- [981. Time Based Key-Value Store](https://leetcode.com/problems/time-based-key-value-store)

## Solution

### 1. Using Hash Map with Array

```Python
class TimeMap:

    def __init__(self):
        # {key: []}, index=timestamp / element=value
        self.records = {}

    # Time complexity: O(T)
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.records:
            latest_timestamp = len(self.records[key])
            latest_value = self.records[key][-1]

            for _ in range(timestamp-latest_timestamp):
                self.records[key].append(latest_value)

            self.records[key].append(value)
        else:
            timestamps = [""] * (timestamp + 1)
            timestamps[timestamp] = value
            self.records[key] = timestamps

    # Time complexity: O(1)
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.records:
            return ""

        if timestamp >= len(self.records[key]):
            return self.records[key][-1]

        return self.records[key][timestamp]
```

> N refers the number of calls and T refers the maximum timestamp

- Time complexity is O(N \* T).
- Space complexity is O(T).

### 2. Using Hash Map with Binary Search

```Python
class TimeMap:

    def __init__(self):
        # {key: [(timestamp, value)]}
        self.records = {}

    # Time complexity: O(1)
    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.records:
            self.records[key] = []

        self.records[key].append((timestamp, value))

    # Time complexity: O(logN)
    def get(self, key: str, timestamp: int) -> str:
        if not key in self.records:
            return ""

        left = 0
        right = len(self.records[key])
        while left < right:
            mid = (left + right) // 2
            if self.records[key][mid][0] <= timestamp:
                left = mid + 1
            else:
                right = mid

        if right == 0:
            return ""

        return self.records[key][left-1][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
```

> N refers the number of calls and T refers the maximum timestamp

- Time complexity is O(N \* logN).
- Space complexity is O(N).
