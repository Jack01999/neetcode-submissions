# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        sortedList = []
        # Search left, node, then right. (1 -> 2 -> 3)
        def dfs(curr):
            if not curr:
                return
            if curr.left:
                dfs(curr.left)
            sortedList.append(curr.val)
            if curr.right:
                dfs(curr.right)

        dfs(root)
        return sortedList[k-1]
        