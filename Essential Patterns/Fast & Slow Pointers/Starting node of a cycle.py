class MyLinkedList:
    def __init__(self, data):
        self.data= data
        self.next= None

    @staticmethod
    def create_list(arr):
        if not arr:
            return None
        head= MyLinkedList(arr[0])
        current=head
        for val in arr[1:]:
            current.next= MyLinkedList(val)
            current= current.next
        return head
    
    @staticmethod
    def create_cycle(head,pos):
        if pos ==-1:
            return head
        index=0
        current=head
        cycle_start= None
        while current:
            if index==pos:
                cycle_start= current
            if not current.next:
                break
            current= current.next
            index+=1
        if cycle_start:
            current.next= cycle_start
        return head
    
    @staticmethod
    def detect_cycle_start(head):
        slow= fast= head
        #Step-1:detect cycle
        while fast and fast.next:
            slow= slow.next
            fast= fast.next.next
            if fast== slow:
                break
        else:
            return None
            
        #Step-2: Find Cycle Start
        slow= head
        while slow != fast:
            slow= slow.next
            fast= fast.next

        return slow
    


head= MyLinkedList.create_list([100,200,300,400,500])
head= MyLinkedList.create_cycle(head, 3)
cycle_start= MyLinkedList.detect_cycle_start(head)
if cycle_start:
    print("Cycle starts at node:",cycle_start.data)
else:
    print("No cycle detected.")

            


    
        
