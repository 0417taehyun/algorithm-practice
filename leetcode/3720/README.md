# 3720. Lexicographically Smallest Permutation Greater Than Target

## Problem

- [3720. Lexicographically Smallest Permutation Greater Than Target](https://leetcode.com/problems/lexicographically-smallest-permutation-greater-than-target)

## Solution

### 1. Using Enumeration

```Python
class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        # {alphabet: count}
        alphabets = {}
        for alphabet in s:
            if alphabet not in alphabets:
                alphabets[alphabet] = 0
            alphabets[alphabet] += 1

        answer = ""
        sorted_alphabets = sorted(alphabets.keys())
        for idx, target_alphabet in enumerate(target):
            # Add the same alphabet in the current position
            if target_alphabet in alphabets and alphabets[target_alphabet] > 0:
                alphabets[target_alphabet] -= 1

                remained_permutation = ""
                for alphabet, count in sorted(alphabets.items(), reverse=True):
                    if count > 0:
                        remained_permutation += (alphabet * count)

                # If the largest permutation with remained alphabets is greater than the remained target alphabets,
                # we can add the same alphabet in the current position
                if remained_permutation > target[idx+1:]:
                    answer += target_alphabet
                    continue

                alphabets[target_alphabet] += 1

            for compare_alphabet in sorted_alphabets:
                # Add the nearest larger alphabet in the current position
                if compare_alphabet > target_alphabet and alphabets[compare_alphabet] > 0:
                    answer += compare_alphabet
                    alphabets[compare_alphabet] -= 1

                    # Add the smallest permutation with remained alphabets
                    for remained_alphabet in sorted_alphabets:
                        count = alphabets[remained_alphabet]
                        if count > 0:
                            answer += (remained_alphabet * count)

                    return answer

            return ""

        return ""

```

> K refers the number of distinct alphabets

- Time complexity is O(N\*K).
- Space complexity is O(K).
