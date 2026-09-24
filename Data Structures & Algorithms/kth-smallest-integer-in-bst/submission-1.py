# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Build the tree, preorder
        bstList = []
        def dfs(curr):
            if not curr:
                return
            # Left
            if curr.left:
                dfs(curr.left)
            # Curr
            bstList.append(curr.val)
            # Right
            if curr.right:
                dfs(curr.right)

        dfs(root)
        
        return bstList[k-1]
        