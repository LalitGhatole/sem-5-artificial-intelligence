from queue import PriorityQueue

def best_first_search(graph, start, goal):
    visited = set()
    priority_queue = PriorityQueue()
    priority_queue.put((0, start))
    
    while not priority_queue.empty():
        cost, current_node = priority_queue.get()
        if current_node == goal:
            return f"Goal {goal} reached with cost {cost}"  # Goal reached
        if current_node in visited:
            continue
        visited.add(current_node)
        
        for neighbor, neighbor_cost in graph[current_node]:
            if neighbor not in visited:
                total_cost = cost + neighbor_cost
                priority_queue.put((total_cost, neighbor))
    
    return f"No path to goal {goal} found"  # Goal not reached

# Example usage:
graph = {
    'A': [('B', 3), ('C', 5)],
    'B': [('D', 2), ('E', 4)],
    'C': [('F', 6)],
    'D': [('G', 1)],
    'E': [],
    'F': [('G', 3)],
    'G': []
}

start_node = 'A'
goal_node = input("Enter the goal node: ")  # Input for the goal state

result = best_first_search(graph, start_node, goal_node)
print(result)
