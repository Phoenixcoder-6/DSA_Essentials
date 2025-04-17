class Queue:
    def __init__(self):
        self.queue=[]
    def enqueue(self,x):
        self.queue.append(x)
    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue.pop(0)
    def peek(self):
        if self.isEmpty():
            return "Queue is Empty"
        return self.queue[0]
    def isEmpty(self):
        return len(self.queue)==0
    def size(self):
        return len(self.queue)
    

q=Queue()
q.enqueue(100)
q.enqueue(202)
q.enqueue(305)
print("Front:", q.peek())     
print("Removed:", q.dequeue()) 
print("Front:", q.peek())       
print("Size:", q.size())   

    
    

