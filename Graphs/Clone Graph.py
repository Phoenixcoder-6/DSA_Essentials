class Node:
    def __init__(self,val=0,neighbors=None):
        self.val= val
        self.neighbors=neighbors if neighbors is not None else []

def clone(node):
    if not node:
        return None
    old_to_new={}

    def dfs(current):
        if current in old_to_new:
            return old_to_new[current]
        copy=Node(current.val)
        old_to_new[current]=copy

        for neighbor in current.neighbors:
            copy.neighbors.append(dfs(neighbor))

        return copy
    
    return dfs(node)
def print_graph(node):
    visited = set()
    def dfs(n):
        if n in visited:
            return
        visited.add(n)
        print(f"Node {n.val} has neighbors: {[neigh.val for neigh in n.neighbors]}")
        for neigh in n.neighbors:
            dfs(neigh)
    dfs(node)

node1= Node(1)
node2= Node(2)
node3= Node(3)
node4= Node(4)

node1.neighbors = [node2, node4]
node2.neighbors = [node1, node3]
node3.neighbors = [node2, node4]
node4.neighbors = [node1, node3]


input_node= node1

cloned_graph= clone(input_node)
print_graph(cloned_graph)



