# 2213. Longest Substring of One Repeating Character

## Problem

- [2213. Longest Substring of One Repeating Character](https://leetcode.com/problems/longest-substring-of-one-repeating-character)

## Solution

### 1. Using Segment Tree

```Python
class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        length = len(s)

        # Information for each node
        prefix = [0] * (4 * length)
        suffix = [0] * (4 * length)
        max_length = [0] * (4 * length)
        left_character = [""] * (4 * length)
        right_character = [""] * (4 * length)


        def build(node_index: int, left: int, right: int) -> None:
            # Build a leaf node
            if left == right:
                prefix[node_index] = 1
                suffix[node_index] = 1
                max_length[node_index] = 1
                left_character[node_index] = s[left]
                right_character[node_index] = s[right]
                return

            mid = (left + right) // 2

            # Build a left child node
            build(node_index=node_index*2, left=left, right=mid)

            # Build a right child node
            build(node_index=node_index*2+1, left=mid+1, right=right)

            # Add current node's information by merging child nodes
            merge(node_index=node_index, left=left, right=right)


        def merge(node_index: int, left: int, right: right) -> None:
            left_child_index = node_index * 2
            right_child_index = node_index * 2 + 1

            # Merge with child nodes
            prefix[node_index] = prefix[left_child_index]
            suffix[node_index] = suffix[right_child_index]
            left_character[node_index] = left_character[left_child_index]
            right_character[node_index] = right_character[right_child_index]
            max_length[node_index] = max(max_length[left_child_index], max_length[right_child_index])

            mid = (left + right) // 2
            left_child_length = mid - left + 1
            right_child_length = right - mid

            # Boundary
            if right_character[left_child_index] == left_character[right_child_index]:
                # All left child node characters are the same character with the boundary
                if left_child_length == prefix[left_child_index]:
                    prefix[node_index] = prefix[left_child_index] + prefix[right_child_index]

                # All right child node characters are the same character with the boundary
                if right_child_length == suffix[right_child_index]:
                    suffix[node_index] = suffix[left_child_index] + suffix[right_child_index]

                # Update the max length with boundary case
                max_length[node_index] = max(max_length[node_index], prefix[right_child_index]+suffix[left_child_index])


        def update(node_index: int, left: int, right: int, target_index: int, character: str) -> None:
            # Update a target leaf node
            if left == right:
                left_character[node_index] = character
                right_character[node_index] = character
                return

            mid = (left + right) // 2

            # Update a left child node
            if target_index <= mid:
                update(node_index=node_index*2, left=left, right=mid, target_index=target_index, character=character)

            # Update a right child node
            else:
                update(node_index=node_index*2+1, left=mid+1, right=right, target_index=target_index, character=character)

            # Update current node by merging child nodes
            merge(node_index=node_index, left=left, right=right)


        answer = []

        build(node_index=1, left=0, right=length-1)
        for target_index, character in zip(queryIndices, queryCharacters):
            update(node_index=1, left=0, right=length-1, target_index=target_index, character=character)
            answer.append(max_length[1])

        return answer

```

- Time complexity is O(N + k\*logN).
- Space complexity is O(N).
