from collections import deque

class StackImplement:
    def __init__(self):
        self.queue1= deque()   #to hold the current stack elements
        self.queue2= deque()    #temporary queue during push

    def push(self,x):
        self.queue2.append(x)
        while self.queue1:
            self.queue2.append(self.queue1.popleft())
        self.queue1,self.queue2= self.queue2,self.queue1

    def pop(self):
        if self.isEmpty():
            return "Stack is Empty"
        return self.queue1.popleft()
    
    def top(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.queue1[0]
    
    def isEmpty(self):
        return not self.queue1
    def showEle(self):
        if self.isEmpty():
            print("Stack is Empty")
        else:
            print("Stack elements:")
            for ele in self.queue1:
                print(ele,end='->')
        
    


q= StackImplement()
q.push(10)
q.push(20)
q.push(30)
q.push(40)
print("Top:",q.top())
print("Popped:",q.pop())
print("Top:",q.top())
print("Stacked Elements:",q.showEle())



