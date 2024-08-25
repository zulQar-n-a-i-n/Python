def Astar(start, end):
    heuristic = {
        'Arad': 366, 'Bucharest': 0, 'Craiova': 160, 'Dobreta': 242, 'Eforie': 161, 'Fagaras': 176,
        'Giurgiu': 77, 'Hirsova': 151, 'Iasi': 226, 'Lugoj': 244, 'Mehadia': 241, 'Neamt': 234,
        'Oradea': 380, 'Pitesti': 10, 'Rimnicu Vilcea': 193, 'Sibiu': 253, 'Timisoara': 329,
        'Urziceni': 80, 'Vaslui': 199, 'Zerind': 374
    }

    graph = {
        'Oradea': {'Adjacents': {'Zerind': 71, 'Sibiu': 151}},
        'Zerind': {'Adjacents': {'Oradea': 71, 'Arad': 75}},
        'Arad': {'Adjacents': {'Zerind': 75, 'Timisoara': 118, 'Sibiu': 140}},
        'Sibiu': {'Adjacents': {'Oradea': 151, 'Arad': 140, 'Fagaras': 99, 'Rimnicu Vilcea': 80}},
        'Timisoara': {'Adjacents': {'Arad': 118, 'Lugoj': 111}},
        'Lugoj': {'Adjacents': {'Timisoara': 111, 'Mehadia': 70}},
        'Mehadia': {'Adjacents': {'Lugoj': 70, 'Dobreta': 75}},
        'Dobreta': {'Adjacents': {'Mehadia': 75, 'Craiova': 120}},
        'Craiova': {'Adjacents': {'Dobreta': 120, 'Rimnicu Vilcea': 146, 'Pitesti': 138}},
        'Rimnicu Vilcea': {'Adjacents': {'Sibiu': 80, 'Craiova': 146, 'Pitesti': 97}},
        'Pitesti': {'Adjacents': {'Rimnicu Vilcea': 97, 'Craiova': 138, 'Bucharest': 101}},
        'Fagaras': {'Adjacents': {'Sibiu': 99, 'Bucharest': 211}},
        'Bucharest': {'Adjacents': {'Fagaras': 211, 'Pitesti': 101, 'Giurgiu': 90, 'Urziceni': 85}},
        'Giurgiu': {'Adjacents': {'Bucharest': 90}},
        'Urziceni': {'Adjacents': {'Bucharest': 85, 'Hirsova': 98, 'Vaslui': 142}},
        'Hirsova': {'Adjacents': {'Urziceni': 98, 'Eforie': 86}},
        'Eforie': {'Adjacents': {'Hirsova': 86}},
        'Vaslui': {'Adjacents': {'Urziceni': 142, 'Iasi': 92}},
        'Iasi': {'Adjacents': {'Vaslui': 92, 'Neamt': 87}},
        'Neamt': {'Adjacents': {'Iasi': 87}},
    }
    if start and end not in graph:
        print("Invalid node")
        exit(1)

    queue = []

    g_n = {node: float('inf') for node in graph}
    g_n[start] = 0
    queue.append((g_n[start] + heuristic[start], start))

    visited = set()

    while queue:

        queue.sort(key=lambda x: x[0])
        current_weight, node = queue.pop(0)

        if node in visited:
            continue

        visited.add(node)
        print(node, end=" ")

        if node == end:
            print(f'\nDistance from {start} to {end} : {current_weight }')
            exit(1)

        for adjacent in graph[node]['Adjacents']:
            if adjacent not in visited:
                temp_n = g_n[node] + graph[node]['Adjacents'][adjacent]

                if temp_n < g_n[adjacent]:
                    g_n[adjacent] = temp_n
                    f_n = g_n[adjacent] + heuristic[adjacent]
                    queue.append((f_n, adjacent))

Astar('Oradea', 'Bucharest')
