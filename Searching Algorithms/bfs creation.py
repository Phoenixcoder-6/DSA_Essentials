from collections import deque 
class TreeNode:
    def __init__(self,value):
        self.value= value # The value stored in the node
        self.left= None
        self.right= None

def bfs_tree(root):
    if not root:
        return    #if tree is empty, exit
    queue= deque([root])   #initialize the queue with the root node

    while queue:
        current = queue.popleft()
        print(current.value,end=" ")
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

root= TreeNode(1)
root.left= TreeNode(2)
root.right= TreeNode(3)
root.left.left= TreeNode(4)
root.left.right= TreeNode(5)
root.right.left= TreeNode(6)
root.right.right= TreeNode(7)

print("BFS Traversal of the Tree:")
bfs_tree(root)




 





