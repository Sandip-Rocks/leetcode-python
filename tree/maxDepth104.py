"""
https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxHeight = 0

        def inorder(node, height):
            nonlocal maxHeight
            if node is None:
                maxHeight = max(maxHeight, height)
                return
            inorder(node.left, height + 1)
            inorder(node.right, height + 1)

        inorder(root, 0)
        return maxHeight
