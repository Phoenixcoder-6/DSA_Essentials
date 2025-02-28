from collections import deque
class TreeNode:
    def __init__(self,value):
        self.value= value
        self.left= None
        self.right= None

def bfs_tree(root):
    if not root:
        return
    queue= deque([root])
    while queue:
        node= queue.popleft()
        print(node.value,end="")

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


root= TreeNode(1)
root.left= TreeNode(2)
root.right = TreeNode(3)
root.left.left= TreeNode(4)
root.left.right= TreeNode(5)
root.right.right= TreeNode(6)

print("\nBFS Traversal of Tree:")
bfs_tree(root)



