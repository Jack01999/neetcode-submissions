# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Levels, so BFS is best
        if not root:
            return []
        res = []
        queue = deque([root])
        while queue:
            size = len(queue)
            currList = []
            for i in range(size):
                curr = queue.popleft()
                currList.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            res.append(currList)
        
        return res
        
        