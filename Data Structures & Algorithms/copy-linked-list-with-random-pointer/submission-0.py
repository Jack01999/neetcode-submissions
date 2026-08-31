"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        build = head
        nodeMap = {None:None}
        while build:
            newNode = Node(build.val)
            nodeMap[build] = newNode
            build = build.next

        curr = head
        while curr:
            newNode = nodeMap[curr]
            newNode.next = nodeMap[curr.next]
            newNode.random = nodeMap[curr.random]
            curr = curr.next

        return nodeMap[head]
        