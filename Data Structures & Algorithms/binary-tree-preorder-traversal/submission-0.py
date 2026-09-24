# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # DFS - preorder (Curr -> Left -> Right)
        res = []
        def dfs(curr):
            if not curr:
                return
            # Curr
            res.append(curr.val)
            # Left
            if curr.left:
                dfs(curr.left)
            # Right
            if curr.right:
                dfs(curr.right)
        dfs(root)
        return res

        