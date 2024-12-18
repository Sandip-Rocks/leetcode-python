"""
https://leetcode.com/problems/symmetric-tree/description/
https://vimeo.com/994619866/c850ae3cbc
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def Mirror(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
            if root1 is None and root2 is None:
                return True
            if root1 is None or root2 is None:
                return False
            if root1.val != root2.val:
                return False
            return Mirror(root1.left, root2.right) and Mirror(root1.right, root2.left)

        return Mirror(root, root)
