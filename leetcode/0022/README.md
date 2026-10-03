# 22. Generate Parentheses

## Problem

- [22. Generate Parentheses](https://leetcode.com/problems/generate-parentheses)

## Solution

### 1. Backtracking

```Python
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        answer = []


        def dfs(parenthese: list[str], open_cnt: int, close_cnt: int) -> None:
            if open_cnt == n and close_cnt == n:
                answer.append("".join(parenthese))
                return

            # Can open
            if open_cnt + 1 <= n:
                parenthese.append("(")
                dfs(parenthese=parenthese, open_cnt=open_cnt+1, close_cnt=close_cnt)
                parenthese.pop()

            # Can close
            if close_cnt + 1 <= n and (close_cnt + 1) <= open_cnt:
                parenthese.append(")")
                dfs(parenthese=parenthese, open_cnt=open_cnt, close_cnt=close_cnt+1)
                parenthese.pop()

        dfs(parenthese=["("], open_cnt=1, close_cnt=0)
        return answer

```

> I need to learn why the time complexity is O(4^N / sqrt(N)) with Catalan number.

- Time complexity is O(4^N / sqrt(N)).
- Space complexity is O(N).
