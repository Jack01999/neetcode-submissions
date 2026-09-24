# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Traverse through every node.
        # Left child must be in the range of -inf, curr.val
        # Right child must be in the range of curr.val, inf
        bound = (float('-inf'), float('inf'))

        def dfs(curr, leftBound, rightBound):
            if not curr:
                return True
            # Current
            if curr.val <= leftBound or curr.val >= rightBound:
                return False
            return dfs(curr.right, curr.val, rightBound) and dfs(curr.left, leftBound, curr.val)

        return dfs(root, bound[0], bound[1])