from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head.next

        prev = None
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        curr = slow.next
        prev = None
        while curr:
            new_node = curr.next
            curr.next = prev
            prev = curr
            curr = new_node

        while prev:
            if prev.val != head.val:
                return False

            prev = prev.next
            head = head.next
          
        return True

