from collections import deque

def bfs(graph, start):

    queue = deque([start])

    visited = set()


    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=" ")


        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B', 'H'],
    'F': ['C'],
    'G': ['C'],
    'H': ['E']
}

bfs(graph, 'A')
