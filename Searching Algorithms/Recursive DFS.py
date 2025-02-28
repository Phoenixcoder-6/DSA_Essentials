def dfs_recursive(graph,node,visited=None):
    if visited is None:
        visited=set()
    visited.add(node)
    print(node,end="")

    for neighbor in graph.get(node,[]):
        if neighbor not in visited:
            dfs_recursive(graph,neighbor,visited)


graph= {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print("DFS Recursive Traversal:")
dfs_recursive(graph,'A')
