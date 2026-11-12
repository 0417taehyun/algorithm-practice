# 3105. Longest Strictly Increasing or Strictly Decreasing Subarray

## Problem

- [3105. Longest Strictly Increasing or Strictly Decreasing Subarray](https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray)

## Solution

### 1. Using One-pass Loop

```Python
class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        answer = 1
        is_asc = None
        subarray = []
        for num in nums:
            if not subarray:
                subarray.append(num)
            else:
                if subarray[-1] == num:
                    answer = max(answer, len(subarray))
                    subarray = [num]
                elif subarray[-1] > num:
                    if is_asc is None:
                        subarray.append(num)
                    elif is_asc:
                        answer = max(answer, len(subarray))
                        subarray = [subarray[-1], num]
                    else:
                        subarray.append(num)

                    is_asc = False
                else:
                    if is_asc is None:
                        subarray.append(num)
                    elif is_asc:
                        subarray.append(num)
                    else:
                        answer = max(answer, len(subarray))
                        subarray = [subarray[-1], num]

                    is_asc = True

        return max(answer, len(subarray))

```

- Time complexity is O(N).
- Space complexity is O(N).

### 2. Space Optimization

```Python
class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        answer, asc, desc = 1, 1, 1
        for idx in range(len(nums)-1):
            if nums[idx] > nums[idx+1]:
                asc = 1
                desc += 1
            elif nums[idx] < nums[idx+1]:
                asc += 1
                desc = 1
            else:
                asc, desc = 1, 1

            answer = max(answer, asc, desc)

        return answer

```

- Time complexity is O(N).
- Space complexity is O(1).
