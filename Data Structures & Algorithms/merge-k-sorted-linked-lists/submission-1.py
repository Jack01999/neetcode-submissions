# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeLists(self, list1: Optional[ListNode], list2: Optional[ListNode]):
        newNode = ListNode()
        res = newNode
        while list1 and list2:
            if list1.val <= list2.val:
                newNode.next = list1
                list1 = list1.next
            else:
                newNode.next = list2
                list2 = list2.next
            newNode = newNode.next
        if list1:
            newNode.next = list1
        else:
            newNode.next = list2
        return res.next
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        while len(lists) > 1:
            list1 = lists.pop(0)
            list2 = lists.pop(0)
            # merge first two, append the result into the list
            mergedNode = self.mergeLists(list1, list2)
            curr = mergedNode
            while curr:
                curr = curr.next
            lists.append(mergedNode)
            # Remove the two lists that were merged
    

        # Return the final list
        return lists[0]
        