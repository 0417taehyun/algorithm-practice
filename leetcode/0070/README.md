# 70. Climbing Stairs

## Problem

- [70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs)

## Solution

### 1. Dynamic Programming

```Python
class Solution:
    def climbStairs(self, n: int) -> int:
        step1, step2 = 1, 1
        for _ in range(1, n):
            step1, step2 = step1+step2, step1
        return step1

```

- Time complexity is O(N).
- Space complexity is O(1).

### 2. Matrix Exponentiation

```Python
class Solution:
    def climbStairs(self, n: int) -> int:
        def matrix_mul(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
            result = [[0, 0], [0, 0]]
            for i in range(2):
                for j in range(2):
                    for k in range(2):
                        result[i][j] += A[i][k] * B[k][j]

            return result


        def matrix_pow(A: List[List[int]], n: int) -> List[List[int]]:
            # Identity Matrix
            result = [[1, 0], [0, 1]]

            while n > 0:
                if n % 2 == 1:
                    result = matrix_mul(A=A, B=result)

                A = matrix_mul(A=A, B=A)
                n //= 2

            return result


        A = [[1, 1], [1, 0]]
        return matrix_pow(A=A, n=n)[0][0]

```

- Time complexity is O(logN).
- Space complexity is O(1).
