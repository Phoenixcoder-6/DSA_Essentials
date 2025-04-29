from collections import deque

queue=deque([10,20,30,40,50])
for items in queue:
    print(items)
def dequeue(queue):
    if len(queue)>0:
        return queue.popleft()
    else:
        return None

x=dequeue(queue)
print("removed element:", x)
