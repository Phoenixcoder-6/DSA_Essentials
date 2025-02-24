from collections import deque
class TreeNode():
    def __init__(self,value):
        self.value= value
        self.left= None
        self.right= None

def level_order_traversal(root):
    if not root:
        return []
    result=[]
    queue= deque([root])    #Initialize queue with root

    while queue:
        node= queue.popleft()
        result.append(node.value)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return result

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(4)
root.left.left = TreeNode(3)
root.left.right = TreeNode(6)
root.right.right = TreeNode(5)

print(level_order_traversal(root))  


