# 509. Fibonacci Number

## Problem

- [509. Fibonacci Number](https://leetcode.com/problems/fibonacci-number)

## Solution

### 1. Dynamic Programming

```Python
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0

        f0, f1 = 0, 1
        for _ in range(2, n+1):
            f0, f1 = f1, f0+f1
        return f1

```

- Time complexity is O(N).
- Space complexity is O(1).

### 2. Matrix Exponentiation

```Python
class Solution:
    def fib(self, n: int) -> int:
        def matrix_mul(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
            result = [[0, 0], [0, 0]]
            for i in range(2):
                for j in range(2):
                    for k in range(2):
                        result[i][j] += (A[i][k] * B[k][j])
            return result


        def matrix_pow(A: List[List[int]], n: int) -> List[List[int]]:
            result = [[1, 0], [0, 1]]
            while n > 0:
                if n % 2 == 1:
                    result = matrix_mul(A=A, B=result)
                    n -= 1

                A = matrix_mul(A=A, B=A)
                n //= 2
            return result


        if n == 0 or n == 1:
            return n

        return matrix_pow(A=[[1, 1], [1, 0]], n=n-1)[0][0]

```

- Time complexity is O(logN).
- Space complexity is O(logN).
