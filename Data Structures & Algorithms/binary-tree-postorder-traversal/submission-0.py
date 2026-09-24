# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # DFS - Postorder (Left -> Right -> Curr)
        res = []

        def dfs(curr):
            if not curr:
                return
            # Left
            dfs(curr.left)
            # Right
            dfs(curr.right)
            # Curr
            res.append(curr.val)

        dfs(root)
        return res
        