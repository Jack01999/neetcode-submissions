# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        res = root
        while True:
            # Left - Traverse left
            if val > res.val:
                if not res.right:
                    res.right = TreeNode(val)
                    return root
                res = res.right
            # Right - Traverse right
            else:
                if not res.left:
                    res.left = TreeNode(val)
                    return root
                res = res.left
            
        