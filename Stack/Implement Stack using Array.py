class StackArray:
    def __init__(self, capacity):
        self.stack= [None] * capacity
        self.top= -1
        self.capacity= capacity

    def push(self,data):
        if self.top == self. capacity- 1 :
            raise Exception("Stack Overflow")
        else:
            self.top +=1
            self.stack[self.top] = data

    def pop(self):
        if self.top == -1:
            raise Exception("Stack Underflow")
        else:
            data= self.stack[self.top]
            self.top -= 1
            return data
        
    def peak(self):
        if self.top == -1:
            raise Exception("Stack Empty")
        data= self.stack[self.top]
        return data
    

arr= StackArray(9)
arr.push(1)
arr.push(2)
arr.push(3)
arr.push(4)
arr.push(5)
arr.pop()
print(arr.peak())


