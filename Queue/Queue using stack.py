class Queue:
    def __init__(self):
        self.stack1=[]
        self.stack2=[]
    def enqueue(self,x):
        self.stack1.append(x)
    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()
    
    def peek(self):
        if self.isEmpty():
            return "Queue is empty."
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]
    def isEmpty(self):
        return not self.stack1 and not self.stack2
    


q= Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print("Front:", q.peek())
print("Removed:", q.dequeue())
print("Peek:", q.peek())
