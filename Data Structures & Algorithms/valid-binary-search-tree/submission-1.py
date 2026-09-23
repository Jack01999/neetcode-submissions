# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        valid = True
        def dfs(curr, left, right) -> bool:
            nonlocal valid
            if not curr:
                return True
            if curr.val <= left or curr.val >= right:
                return False
            if curr.left:
                valid = dfs(curr.left, left, curr.val)
            if curr.right:
                valid = dfs(curr.right, curr.val, right)
            return valid

        return dfs(root, float('-inf'), float('inf'))