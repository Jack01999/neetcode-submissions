# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # DFS - preorder
        # Keep track of the max of the current node
        res = 0

        def dfs(curr, currMax):
            nonlocal res
            if curr.val >= currMax:
                # print(curr.val)
                res += 1
            if curr.left:
                dfs(curr.left, max(curr.val, currMax))
            if curr.right:
                dfs(curr.right, max(curr.val, currMax))
            
        dfs(root, -101)

        return res



        