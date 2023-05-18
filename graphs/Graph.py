from LinkedList import LinkedList
from Node import Node

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.list = [LinkedList() for i in range(vertices)]

    def add_edge(self, source, dest):
        if (source >= 0 and dest >= 0 and
            source < self.vertices and dest < self.vertices):
            self.list[source].insert_at_head(dest)

    def print(self):
        print(">>Adjacency List of Directed Graph<<")
        for i in range(self.vertices):
            print("|", i, end=" | => ")
            cur = self.list[i].head
            while cur is not None:
                print("[", cur.val, end=" ] -> ")
                cur = cur.next
            print("None")
    
    def bfs(self):
        start = Node(1)
        seen = {}
        queue = [start]
        res = [1]
        while queue:
            top = queue.pop()
            current = self.list[top.val].head
            while current:
                if current.val not in seen:
                    seen[current.val] = True
                    queue.append(current)
                    res.append(current.val)
                current = current.next
        return res 

graph = Graph(7)
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 4)
graph.add_edge(3, 4)
graph.add_edge(3, 5)
graph.add_edge(3, 6)
graph.add_edge(6, 1)
graph.print()
print(graph.bfs())
