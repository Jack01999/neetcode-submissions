# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queueP = deque([p])
        queueQ = deque([q])

        while queueP and queueQ:
            currP = queueP.popleft()
            currQ = queueQ.popleft()
            # Both None
            if not currP and not currQ:
                continue
            # Either is None (unequal) or values are not equal
            if not currP or not currQ or currP.val != currQ.val:
                return False
            # Neither are None and values are equal
            queueP.append(currP.left)
            queueP.append(currP.right)
            queueQ.append(currQ.left)
            queueQ.append(currQ.right)
            
        
        return True