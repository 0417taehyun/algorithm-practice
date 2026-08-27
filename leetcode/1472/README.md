# 1472. Design Browser History

## Problem

- [1472. Design Browser History](https://leetcode.com/problems/design-browser-history/description/)

## Solution

### 1. Using Doubly-Linked List

```Python
class Browser:

    def __init__(self, url: str, prev: Optional["Browser"] = None, next: Optional["Browser"] = None):
        self.url = url
        self.prev = prev
        self.next = next


class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr = Browser(url=homepage)

    def visit(self, url: str) -> None:
        browser = Browser(url=url, prev=self.curr, next=None)
        self.curr.next = browser
        self.curr = browser

    def back(self, steps: int) -> str:
        while steps > 0 and self.curr.prev is not None:
            self.curr = self.curr.prev
            steps -= 1
        return self.curr.url

    def forward(self, steps: int) -> str:
        while steps > 0 and self.curr.next is not None:
            self.curr = self.curr.next
            steps -= 1
        return self.curr.url


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
```

> It takes O(N) for `back` and `forward` method to traverse the nodes.

- Time complexity is O(N).
- Space complexity is O(N).

### 2. Using Dynamic Array

```Python
class BrowserHistory:

    def __init__(self, homepage: str):
        self.histories = [homepage]
        self.curr = 0
        self.size = 1

    def visit(self, url: str) -> None:
        # Append at the end
        if self.curr == len(self.histories) - 1:
            self.histories.append(url)
            self.size += 1
        else:
            self.histories[self.curr+1] = url
            self.size = self.curr + 2

        self.curr += 1

    def back(self, steps: int) -> str:
        self.curr = max(0, self.curr-steps)
        return self.histories[self.curr]

    def forward(self, steps: int) -> str:
        self.curr = min(self.size-1, self.curr+steps)
        return self.histories[self.curr]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)

```

> It takes O(1) for `back` and `forward` method to traverse the nodes.

- Time complexity is O(1).
- Space complexity is O(1).
