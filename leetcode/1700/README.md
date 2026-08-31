# 1700. Number of Students Unable to Eat Lunch

## Problem

- [1700. Number of Students Unable to Eat Lunch](https://leetcode.com/problems/number-of-students-unable-to-eat-lunch)

## Solution

### 1. Using Queue

```Python
class Student:
    def __init__(self, pref: int, prev: Optional["Student"] = None, next: Optional["Student"] = None):
        self.pref = pref
        self.prev = prev
        self.next = next


class Queue:
    def __init__(self):
        self.size = 0
        self.head = Student(pref=-1)
        self.tail = Student(pref=-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def enqueue(self, pref: int) -> None:
        student = Student(pref=pref, prev=self.tail.prev, next=self.tail)
        self.tail.prev.next = student
        self.tail.prev = student
        self.size += 1

    def dequeue(self) -> Optional[Studet]:
        if self.head.next == self.tail:
            return None

        student = self.head.next
        self.head.next.next.prev = self.head
        self.head.next = self.head.next.next
        self.size -= 1

        return student

    def get_size(self) -> int:
        return self.size


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        queue = Queue()
        for pref in students:
            queue.enqueue(pref=pref)

        for sandwich in sandwiches:
            count = 1
            size = queue.get_size()
            student = queue.dequeue()
            while student is not None:
                if sandwich == student.pref:
                    break

                # Leave and go to the queue's end
                queue.enqueue(pref=student.pref)

                # All students do not want to take the top sandwich
                if count == size:
                    return size

                # Check next student
                student = queue.dequeue()
                count += 1

        return queue.get_size()
```

- Time complexity is O(N^2).
- Space complexity is O(N).

### 2. Using Hash Map

```Python
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # {sandwich: count}
        counter = {}
        for preference in students:
            if preference not in counter:
                counter[preference] = 0
            counter[preference] += 1

        for sandwich in sandwiches:
            if sandwich in counter and counter[sandwich] > 0:
                counter[sandwich] -= 1
            else:
                break

        return sum(counter.values())
```

- Time complexity is O(N).
- Space complexity is O(N).
