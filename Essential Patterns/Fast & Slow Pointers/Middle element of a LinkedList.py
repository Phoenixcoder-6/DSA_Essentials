class MyLinkedList:
    def __init__(self,data):
        self.data= data
        self.next= None

    @staticmethod
    def create_list(arr):
        if not arr:
            return None
        head= MyLinkedList(arr[0])
        current= head
        for val in arr[1:]:
            current.next = MyLinkedList(val)
            current= current.next
        return head
    
    @staticmethod
    def find_middle(head):
        if not head:
            return None
        slow=fast=head
        while fast and fast.next:
            slow= slow.next
            fast= fast.next.next

        return slow
    
head= MyLinkedList.create_list([100,200,300,400,500])
middle= MyLinkedList.find_middle(head)
if middle:
    print("Middle node:", middle.data)
else:
    print("Empty list!")



