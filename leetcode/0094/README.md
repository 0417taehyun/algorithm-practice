# 94. Binary Tree Inorder Traversal

## Problem

- [94. Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal)

## Solution

### 1. Recursion

```Python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        answer = []


        def inorder(node: Optional[TreeNode]) -> None:
            if node is None:
                return None

            inorder(node=node.left)
            answer.append(node.val)
            inorder(node=node.right)


        inorder(node=root)
        return answer

```

- Time complexity is O(N).
- Space complexity is O(N).
