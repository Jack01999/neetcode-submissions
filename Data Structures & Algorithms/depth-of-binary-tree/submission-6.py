# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        # Preorder
        res = 0
        leftMax = 0
        rightMax = 0

        if root.left:
            leftMax = self.maxDepth(root.left)
        if root.right:
            rightMax = self.maxDepth(root.right)
        return 1 + max(leftMax, rightMax)

        