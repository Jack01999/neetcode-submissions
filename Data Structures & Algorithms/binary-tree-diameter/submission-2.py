# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiameter = 0

        def dfs(root):
            nonlocal maxDiameter
            if root == None:
                return 0
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            maxDiameter = max(maxDiameter, leftMax + rightMax)
            return max(leftMax, rightMax) + 1
        
        dfs(root)
        return maxDiameter
        