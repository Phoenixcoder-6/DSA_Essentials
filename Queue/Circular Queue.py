class CircularQueue:
    def __init__(self,k):
        self.queue=[None]*k
        self.front=-1
        self.rear=-1
        self.size=k


    def isEmpty(self):
        return self.front==-1
    
    def isFull(self):
        return (self.rear+1) % self.size == self.front
    
    def enqueue(self,x):
        if self.isFull():
            return "Queue is Full"
        if self.isEmpty():
            self.front=0
        self.rear= (self.rear+1) % self.size
        self.queue[self.rear] =x

    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        removed = self.queue[self.front]
        if self.front== self.rear:
            self.front= self.rear= -1
        else:
            self.front =(self.front +1) % self.size
        return removed
    


    def getfront(self):
        if self.isEmpty():
            return " Queue is empty"
        return self.queue[self.front]
    
    def getrear(self):
        if self.isEmpty():
            return "Queue is Empty"
        return self.queue[self.rear]
    

cq = CircularQueue(3)
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
print(cq.enqueue(40))     
print("Front:", cq.getfront())  
print("Rear:", cq.getrear())    
print("Removed:", cq.dequeue())  
cq.enqueue(40)
print("Rear after enqueue 40:", cq.getrear()) 
      


    