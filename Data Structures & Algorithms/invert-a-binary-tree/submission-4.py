# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Preorder
        res = root
        def dfs(curr):
            if not curr:
                return
            # Self (Swap left and right children)
            temp = curr.left
            curr.left = curr.right
            curr.right = temp
            # Left
            if curr.left:
                dfs(curr.left)
            # Right
            if curr.right:
                dfs(curr.right)
        dfs(root)
        return res
        