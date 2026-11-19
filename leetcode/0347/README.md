# 347. Top K Frequent Elements

## Problem

- [347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements)

## Solution

### 1. Using Heap

```Python
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        return heapq.nlargest(k, counter.keys(), counter.get)

```

- Time complexity is O(NlogN).
- Space complexity is O(N).

### 2. Using Bucket Sort

```Python
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        bucket_size = max(counter.values())
        buckets = [[] for count in range(bucket_size+1)]
        for number, count in counter.items():
            buckets[count].append(number)

        answer = []
        for bucket in buckets[::-1]:
            for number in bucket:
                answer.append(number)
                if len(answer) == k:
                    return answer

```

- Time complexity is O(N).
- Space complexity is O(N).
