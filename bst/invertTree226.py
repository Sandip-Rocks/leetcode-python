# https://leetcode.com/problems/invert-binary-tree/
# https://vimeo.com/994619866/c850ae3cbc

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        # Swap the left and right children
        root.left, root.right = root.right, root.left

        # Recursively invert the left and right subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

# Example usage:
# Constructing a binary tree
#         4
#        / \
#       2   7
#      / \ / \
#     1  3 6  9


# Inverting the binary tree
# After inversion:
#         4
#        / \
#       7   2
#      / \ / \
#     9  6 3  1
