class LinkedList:
    def __init__(self, val=0, next=None):  
        self.val = val
        self.next = next
        
class MyLinkedList:
    def __init__(self):
        self.dummy = LinkedList()
        self.size = 0
     
    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1  
        curr = self.dummy.next
        for _ in range(index):
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)
        
    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:  

            return 

        predecessor = self.dummy
        for _ in range(index):
            predecessor = predecessor.next
        new_node = LinkedList(val, predecessor.next)
        predecessor.next = new_node

        self.size += 1 
    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:  
            return 
        
        predecessor = self.dummy
        for _ in range(index):
            predecessor = predecessor.next
        
        predecessor.next = predecessor.next.next
        self.size -= 1  