# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        solution = ListNode()
        head = solution

        while list1 != None and list2 != None:
            if list1.val <= list2.val:
                newNode = ListNode(val=list1.val)
                solution.next = newNode
                solution = solution.next
                list1 = list1.next
            else:
                newNode = ListNode(val=list2.val)
                solution.next = newNode
                solution = solution.next
                list2 = list2.next

        # Add the rest of list1/list2, whichever one is not null
        if list1 != None:
            while list1 != None:
                newNode = ListNode(val=list1.val)
                solution.next = newNode
                solution = solution.next
                list1 = list1.next
        if list2 != None:
            while list2 != None:
                newNode = ListNode(val=list2.val)
                solution.next = newNode
                solution = solution.next
                list2 = list2.next

        return head.next
        