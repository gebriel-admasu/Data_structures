# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = []
        while list1 is not None:
            res.append(list1.val)
            list1 = list1.next
        while list2 is not None:
            res.append(list2.val)
            list2 = list2.next
        
        res.sort()

        dummy = ListNode(-1)
        curr = dummy
        for value in res:
            
            curr.next = ListNode(value)
            curr = curr.next

        return dummy.next

      