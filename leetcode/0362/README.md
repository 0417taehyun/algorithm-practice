# 362. Design Hit Counter

## Problem

- [362. Design Hit Counter](https://leetcode.com/problems/design-hit-counter)

## Solution

### 1. Using Circular Buffer

```Python
class HitCounter:

    def __init__(self):
        self.threshold = 300
        self.buckets = []

        for timestamp in range(self.threshold):
            self.buckets.append([timestamp, 0])

    def hit(self, timestamp: int) -> None:
        idx = timestamp % 300
        if self.buckets[idx][0] == timestamp:
            self.buckets[idx][1] += 1
        else:
            self.buckets[idx][0] = timestamp
            self.buckets[idx][1] = 1

    def getHits(self, timestamp: int) -> int:
        total = 0
        for stored_timestamp, count in self.buckets:
            if stored_timestamp + self.threshold > timestamp:
                total += count
        return total


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)

```

> T refers threashold, which is 300 in this problem

- Time complexity is O(T).
- Space complexity is O(T).
