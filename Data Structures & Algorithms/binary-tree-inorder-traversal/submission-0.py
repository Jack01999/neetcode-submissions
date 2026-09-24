# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # DFS - Inorder
        res = []
        def dfs(curr):
            if not curr:
                return
            # Left
            if curr.left:
                dfs(curr.left)
            # Curr
            res.append(curr.val)
            # Right
            if curr.right:
                dfs(curr.right)
        dfs(root)
        return res
        