from collections import deque
def reverse_first_k(queue,k):
    if k<=0 or k>len(queue):
        return queue
    stack=[]
    for _ in range(k):
        stack.append(queue.popleft())
    while stack:
        queue.append(stack.pop())
    for _ in range(len(queue)-k):
        queue.append(queue.popleft())

    return queue

queue=deque([10,20,30,40,50])
k=4
result= reverse_first_k(queue,k)
print("Queue after reversing first k elements:", list(result))
