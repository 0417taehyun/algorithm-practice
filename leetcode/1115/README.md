# 1115. Print FooBar Alternately

## Problem

- [1115. Print FooBar Alternately](https://leetcode.com/problems/print-foobar-alternately)

## Solution

### 1. Using Lock

```Python
from threading import Lock


class FooBar:
    def __init__(self, n):
        self.n = n
        self.locks = (Lock(), Lock())
        self.locks[1].acquire()

    def foo(self, printFoo: 'Callable[[], None]') -> None:

        for i in range(self.n):
            self.locks[0].acquire()
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.locks[1].release()


    def bar(self, printBar: 'Callable[[], None]') -> None:

        for i in range(self.n):
            self.locks[1].acquire()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.locks[0].release()

```
