"""
https://leetcode.com/problems/sum-of-left-leaves/

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        self.total_sum = 0

        def inorder(node):
            if node is None:
                return
            inorder(node.left)

            if node.left and node.left.left is None and node.left.right is None:
                self.total_sum += node.left.val

            inorder(node.right)

        inorder(root)
        return self.total_sum
