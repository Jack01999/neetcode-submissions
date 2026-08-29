# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        head = res
        while list1 != None and list2 != None:
            if list1.val <= list2.val:
                # Add list1 Node to res
                newNode = ListNode(val=list1.val)
                res.next = newNode
                # Traverse
                list1 = list1.next
                res = res.next
            else:
                # Add list2 Node to res
                newNode = ListNode(val=list2.val)
                res.next = newNode
                # Traverse
                list2 = list2.next
                res = res.next

        if list1 == None:
            while list2 != None:
                newNode = ListNode(val=list2.val)
                res.next = newNode
                list2 = list2.next
                res = res.next
        else:
            while list1 != None:
                newNode = ListNode(val=list1.val)
                res.next = newNode
                list1 = list1.next
                res = res.next

        return head.next


        