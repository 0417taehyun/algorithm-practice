# 1807. Evaluate the Bracket Pairs of a String

## Problem

- [1807. Evaluate the Bracket Pairs of a String](https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string)

## Solution

### 1. Using Hash Map

```Python
class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        knowledges = {}
        for key, value in knowledge:
            knowledges[key] = value

        answer = ""
        record = ""
        should_record = False
        for character in s:
            if character == "(":
                should_record = True
            elif character == ")":
                should_record = False
                if record in knowledges:
                    answer += knowledges[record]
                else:
                    answer += "?"
                record = ""
            elif should_record:
                record += character
            else:
                answer += character

        return answer

```

- Time complexity is O(N).
- Space complexity is O(N).
