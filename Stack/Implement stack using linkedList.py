class Node:
    def __init__(self,data):
        self.data = data
        self.next= None

class StackLinkedList:
    def __init__(self):
        self.head= None

    def push(self, item):
        new_node= Node(item)
        new_node.next= self.head
        self.head=new_node

    def pop(self):
        if self.head is None:
            raise Exception("Stack Underflow")
        else:
            item= self.head.data
            self.head= self.head.next
            return item
        
    def peek(self):
        if self.head is None:
            raise Exception("Empty Stack")
        return self.head.data
    
arr= StackLinkedList()
arr.push(10)
arr.push(20)
arr.push(30)
print(arr.peek())
