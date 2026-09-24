# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        res = root

        def dfs(curr):
            nonlocal res
            if not curr:
                return
            # current is the LCA
            print('curr val : ', curr.val)
            if p.val <= curr.val and q.val >= curr.val or q.val <= curr.val and p.val >= curr.val:
                #print('completed')
                #print('curr : ', curr.val)
                res = curr
            if p.val < curr.val and q.val < curr.val:
                #print('here')
                dfs(curr.left)
            if p.val > curr.val and q.val > curr.val:
                dfs(curr.right)
            
        dfs(root)
        return res


            
        