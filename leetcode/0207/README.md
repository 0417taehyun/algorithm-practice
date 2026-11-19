# 207. Course Schedule

## Problem

- [207. Course Schedule](https://leetcode.com/problems/course-schedule)

## Solution

### 1. Depth-First Search (DFS)

```Python
class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        course_graph = {course: [] for course in range(numCourses)}
        for course, prerequisite in prerequisites:
            course_graph[course].append(prerequisite)

        visited = set()


        def dfs(course: int) -> bool:
            if course in visited:
                return False

            if not course_graph[course]:
                return True

            visited.add(course)
            for prerequisite in course_graph[course]:
                if not dfs(course=prerequisite):
                    return False

            visited.remove(course)
            course_graph[course] = []
            return True


        for course in range(numCourses):
            if not dfs(course=course):
                return False
        return True

```

> P refers the size of prerequisites

- Time complexity is O(N+P).
- Space complexity is O(N+P).

### 2. Khan's Algorithm

```Python
from collections import deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        course_graph = {course: [] for course in range(numCourses)}
        ingredients = [0] * numCourses

        for course, prerequisite in prerequisites:
            course_graph[prerequisite].append(course)
            ingredients[course] += 1

        queue = deque()
        for course, ingredient in enumerate(ingredients):
            if ingredient == 0:
                queue.append(course)

        while queue:
            prerequisite = queue.popleft()
            numCourses -= 1

            for course in course_graph[prerequisite]:
                ingredients[course] -= 1
                if ingredients[course] == 0:
                    queue.append(course)

        return numCourses == 0

```

- Time complexity is O(N+P).
- Space complexity is O(N+P).
