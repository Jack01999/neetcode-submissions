# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        listLength = 0
        curr = head
        while curr:
            listLength += 1
            curr = curr.next

        toRemove = listLength - n
        if toRemove == 0:
            return head.next

        curr = head
        for i in range(listLength - 1):
            if (i+1) == toRemove:
                curr.next = curr.next.next
                break
            curr = curr.next
        

        return head
        