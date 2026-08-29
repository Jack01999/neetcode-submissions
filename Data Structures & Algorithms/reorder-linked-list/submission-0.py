# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Find middle using slow/fast pointers
# reverse second half
# merge first and second half





class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        # Find middle using slow/fast pointers (Middle is the slow)
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        # Reverse second half (starting at slow)
        curr = slow.next
        prev = slow.next = None
        while curr:
            temp = curr.next
            curr.next = prev
            # Traverse
            prev = curr
            curr = temp

        # merge first and second half (first half = front, second half = prev)
        first, second = head,prev
        while second:
            tempFirst = first.next
            tempSecond = second.next
            first.next = second
            second.next = tempFirst
            first = tempFirst
            second = tempSecond
        # while prev:
        #     temp = front.next
        #     tempPrev = prev.next
        #     front.next = prev
        #     prev.next = front
        #     front = temp
        #     prev = tempPrev

        



    
        