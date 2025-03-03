# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reverse(head: ListNode) -> ListNode:
    prev = None
    curr = head

    while curr:
        next_node = curr.next 
        curr.next = prev  
        prev = curr 
        curr = next_node  

    return prev 
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        if not head:
            return 0 
        
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second_half = reverse(slow)
        
        max_value = 0
        first_half = head
        
        while second_half: 
            total = first_half.val + second_half.val
            max_value = max(max_value, total)
            first_half = first_half.next
            second_half = second_half.next
        
        return max_value
