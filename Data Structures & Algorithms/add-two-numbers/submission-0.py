# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Add numbers together, make sure to consider carry over
        res = curr = ListNode()
        carry = 0
        while l1 and l2:
            sum = l1.val + l2.val + carry
            print(sum)
            if sum > 9:
                sum -= 10
                newNode = ListNode(val=sum)
                carry = 1
            else:
                newNode = ListNode(val=sum)
                carry = 0
            curr.next = newNode
            curr = curr.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            sum = l1.val + carry
            if sum > 9:
                sum -= 10
                newNode = ListNode(val=sum)
                carry = 1
            else:
                newNode = ListNode(val=sum)
                carry = 0
            curr.next = newNode
            curr = curr.next
            l1 = l1.next
        while l2:
            sum = l2.val + carry
            if sum > 9:
                sum -= 10
                newNode = ListNode(val=sum)
                carry = 1
            else:
                newNode = ListNode(val=sum)
                carry = 0
            curr.next = newNode
            curr = curr.next
            l2 = l2.next
        if carry == 1:
            newNode = ListNode(val=carry)
            curr.next = newNode
            curr = curr.next

        return res.next
