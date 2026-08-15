# 49. Group Anagrams

## Problem

- [49. Group Anagrams](https://leetcode.com/problems/group-anagrams)

## Solution

### 1. Using Hash Map

```Python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # (ordered_word: [original_word])
        anagrams = {}
        for idx, word in enumerate(strs):
            ordered_word = "".join(sorted(word))
            if ordered_word in anagrams:
                anagrams[ordered_word].append(word)
            else:
                anagrams[ordered_word] = [word]

        answer = []
        for words in anagrams.values():
            answer.append(words)

        return answer


```

- Time complexity is O(NlogN).
- Space complexity is O(N).
