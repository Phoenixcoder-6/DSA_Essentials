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
            current.next= MyLinkedList(val)
            current= current.next
        return head
    
    @staticmethod
    def detect_cycle(head):
        slow=fast= head
        while fast and fast.next:
            slow= slow.next
            fast= fast.next.next
            if slow==fast:
                return True
        return False
    @staticmethod
    def create_cycle(head,pos):
        if pos==-1:   #handling edge cases
            return head
        cycle_start=None   #stores the node where the cycle should start
        current= head
        index= 0

        while current:
            if index== pos:
                cycle_start=current
            if not current.next:
                break
            current= current.next
            index+=1

        if cycle_start:
            current.next= cycle_start

        return head

    
head = MyLinkedList.create_list([100,200,300,400,500,100])
head= MyLinkedList.create_cycle(head,3)

print(MyLinkedList.detect_cycle(head))


            
        



