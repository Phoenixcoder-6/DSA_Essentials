def dfs_iterative(graph, root):
    visited = set()
    stack = [root]
    
    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end="->")
            visited.add(node)
            stack.extend(reversed(graph.get(node, [])))  # Add unvisited neighbors

# Corrected Graph Dictionary
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C'],
    'G': []  # Missing node added
}

print("DFS Iterative Traversal:")
dfs_iterative(graph, "A")
