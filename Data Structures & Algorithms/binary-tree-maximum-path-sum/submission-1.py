# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Max of left subtree+node.val or right subtree+node.val or leftsubtree+rightsubtree+node.val
        # Keep global to store the max
        globalMax = float('-inf')

        def dfs(node):
            nonlocal globalMax
            if node is None:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            currMax = max(left+node.val, right+node.val, node.val)
            globalMax = max(globalMax, currMax, left+right+node.val)
            return currMax

        dfs(root)
        return globalMax
        