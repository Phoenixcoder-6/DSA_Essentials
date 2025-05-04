from collections import defaultdict
def connected_components(n,edges):
    #initialize adjacency list as an array of arraylists
    graph=[[] for _ in range(n)]
    #build adjacency list
    for u,v in edges:
        graph[u].append(v)
        graph[v].append(u)
    #Visited array
    visited=[False]*n
    #result
    result=[]

    def dfs(node,component):
        visited[node]=True
        component.append(node)
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor,component)
    for i in range(n):
        if not visited[i]:
            component=[]
            dfs(i,component)
            result.append(component)

    return result
n=5
edges=[[0,4],[1,2],[3,4]]
print(connected_components(n,edges))






