# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        
        stack = [root]
        visited = {None: (0, 0)}
        while stack:
            top = stack[-1]
            if top.left and top.left not in visited:
                stack.append(top.left)
            elif top.right and top.right not in visited:
                stack.append(top.right)
            else:
                node = stack.pop()
                leftHeight, leftDiameter = visited[node.left][0], visited[node.left][1]
                rightHeight, rightDiameter = visited[node.right][0], visited[node.right][1]
                visited[node] = (1+max(leftHeight,rightHeight), max(leftHeight+rightHeight, leftDiameter, rightDiameter))
        return visited[root][1]
        
        