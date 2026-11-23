# 1352. Product of the Last K Numbers

## Problem

- [1352. Product of the Last K Numbers](https://leetcode.com/problems/product-of-the-last-k-numbers)

## Solution

### 1. Using Prefix Product

```Python
class ProductOfNumbers:

    def __init__(self):
        self.prefix_product = [1]
        self.size = 0

    def add(self, num: int) -> None:
        if num == 0:
            self.prefix_product = [1]
            self.size = 0
        else:
            prev = self.prefix_product[-1]
            self.prefix_product.append(prev*num)
            self.size += 1

    def getProduct(self, k: int) -> int:
        if k > self.size:
            return 0

        return self.prefix_product[-1] // self.prefix_product[self.size-k]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
```

> Time complexity of add and getProduct are O(1)

- Time complexity is O(N).
- Space complexity is O(N).
