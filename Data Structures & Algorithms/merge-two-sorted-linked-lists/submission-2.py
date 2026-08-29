# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        curr = res
        while list1 != None and list2 != None:
            if list1.val <= list2.val:
                # Add list1 Node to curr
                newNode = ListNode(val=list1.val)
                curr.next = newNode
                # Traverse
                list1 = list1.next
                curr = curr.next
            else:
                # Add list2 Node to curr
                newNode = ListNode(val=list2.val)
                curr.next = newNode
                # Traverse
                list2 = list2.next
                curr = curr.next

        if list1 == None:
            curr.next = list2
        if list2 == None:
            curr.next = list1

        return res.next


        