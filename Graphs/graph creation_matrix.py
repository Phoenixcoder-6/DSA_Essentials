class graph:
    def __init__(self,n):
        self.matrix= [[0] * n for _ in range(n)]

    def add_edge(self,u,v):
        self.matrix[u][v]= 1

    def display(self):
        for row in self.matrix:
            print(row)


g= graph(6)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(0, 5)
g.add_edge(5, 4)

g.display()

