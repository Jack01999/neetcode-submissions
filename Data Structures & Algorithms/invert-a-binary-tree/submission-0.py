# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return None
        curr = root
        visited = [curr]
        while visited:
            node = visited.pop(0)
            if node.left:
                visited.append(node.left)
            if node.right:
                visited.append(node.right)
            
            temp = node.left
            node.left = node.right
            node.right = temp
        return root

        