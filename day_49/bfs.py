from collections import defaultdict

class Graph():
    def __init__(self):
        self.graph = defaultdict(list)
        self.visited = []


    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, s):
        self.queue = [s]
        self.visited.append(s)
        while(len(self.queue) > 0):
            s = self.queue.pop(0)
            print(s)
            for i in self.graph[s]:
                if i not in self.visited:
                    self.queue.append(i)
                    self.visited.append(i)

new_graph = Graph()
new_graph.addEdge(1, 2)
new_graph.addEdge(1, 3)
new_graph.addEdge(2, 3)
new_graph.addEdge(2, 4)
new_graph.addEdge(4, 1)
new_graph.BFS(2)
