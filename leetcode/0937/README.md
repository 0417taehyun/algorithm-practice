# 937. Reorder Data in Log Files

## Problem

- [937. Reorder Data in Log Files](https://leetcode.com/problems/reorder-data-in-log-files)

## Solution

### 1. Sorting

```Python
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit_logs = []
        letter_logs = []

        for log in logs:
            if log.split(" ")[1].isdigit():
                digit_logs.append(log)
            else:
                letter_logs.append(log)

        letter_logs.sort(key=lambda log: (log.split(" ")[1:], log.split(" ")[0]))
        return letter_logs + digit_logs

```

- Time complexity is O(NlogN).
- Space complexity is O(N).
