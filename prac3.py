import heapq

# Define the A* algorithm
def a_star(graph, start, goal):
    open_set = [(0, start)]
    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path

        for neighbor, cost in get_neighbors(graph, current).items():
            tentative_g_score = g_score[current] + cost

            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score, neighbor))

    return None

# Define a function to get neighbors
def get_neighbors(graph, node):
    return graph.get(node, {})

# Define the heuristic function (Manhattan distance)
def heuristic(node, goal):
    H_dist = {'A': 3, 'B': 2, 'C': 2, 'D': 1, 'E': 0}
    return H_dist[node]

# Define the graph
Graph_nodes = {
    'A': {'B': 1, 'C': 3},
    'B': {'A': 1, 'D': 2},
    'C': {'A': 3, 'E': 4},
    'D': {'B': 2},
    'E': {'C': 4}
}

# Find the path from 'A' to 'E'
goal_node = input("Enter the goal node: ")
path = a_star(Graph_nodes, 'A', goal_node)

if path:
    print('Path found:', path)
else:
    print('No path found!')
