# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not q and p:
            return False
        if not p and q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        res = False

        # Traverse through tree
        def dfs(curr):
            nonlocal res
            if not curr:
                return
            # Self
            # Check whether subRoot is same tree at the current node
            if res == False:
                res = self.isSameTree(curr, subRoot)
            # Left
            if curr.left:
                dfs(curr.left)
            # Right
            if curr.right:
                dfs(curr.right)

        dfs(root)

        return res

        
        