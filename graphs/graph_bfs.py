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
            ['h', 'f']
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

# Find path from A -> C
def shortestPath(vertices, start, end):
    if start == end:
        return 1
    queue = deque()
    queue.append(vertices[start])
    visited = set()
    visited.add(start)
    level = 1
    while queue:
        levelLen = len(queue)
        level += 1
        for i in range(levelLen):
            destinations = queue.popleft()
            for dest in destinations:
                if dest == end:
                    print('FOUND:', end, ", level:", level)
                if dest not in visited:
                    print('dest:', dest)
                    queue.append(vertices[dest])
                    visited.add(dest)

ans = shortestPath(graph.vertices, 'a', 'c')
print(ans)
