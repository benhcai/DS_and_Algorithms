from collections import deque

edges = [
            ['a', 'b'],
            ['a', 'e'],
            ['b', 'c'],
            ['b', 'd'],
            ['c', 'f'],
            ['e', 'd'],
            ['d', 'g'],
            ['d', 'h'],
            ['g', 'c'],
            ['h', 'f'],
            ['b', 'i'],
            ['i', 'j'],
            ['k', 'l']
        ]

class Graph:
    def __init__(self, edges):
        self.vertices = {}
        for route in edges:
            for dest in route:
                if dest not in self.vertices:
                    self.vertices[dest] = []
            self.vertices[route[0]].append(route[1])

graph = Graph(edges)
print(graph.vertices)

def shortestPath(vertices, start, end):
    stack = []
    stack.extend(vertices[start])
    visited = set() 
    while stack:
        dest = stack.pop()
        if dest == end:
            print("FOUND: ", end)
        else:
            print("dest: ", dest)
        for place in vertices[dest]:
            if place not in visited:
                visited.add(dest)
                stack.append(place)

shortestPath(graph.vertices, 'a', 'f')
