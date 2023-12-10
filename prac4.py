from queue import PriorityQueue

# Define the goal state
goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]

# Define the initial state
initial_state = [1, 2, 3, 4, 0, 5, 6, 7, 8]

# Define a function to calculate the Manhattan distance for a tile
def manhattan_distance(tile, current_pos):
    if tile == 0:
        return 0
    goal_pos = goal_state.index(tile)
    return abs(current_pos % 3 - goal_pos % 3) + abs(current_pos // 3 - goal_pos // 3)

# Define a function to calculate the total Manhattan distance for the entire board
def total_manhattan_distance(board):
    return sum(manhattan_distance(board[i], i) for i in range(9))

# Define the A* algorithm to solve the puzzle
def solve_puzzle(initial_state):
    open_set = PriorityQueue()
    open_set.put((0, initial_state, []))
    visited = set()

    while not open_set.empty():
        _, current_state, path = open_set.get()
        if current_state == goal_state:
            return path

        zero_pos = current_state.index(0)
        for move in [-1, 1, -3, 3]:
            new_pos = zero_pos + move
            if 0 <= new_pos < 9 and (zero_pos % 3 != 2 or move != 1) and (zero_pos % 3 != 0 or move != -1):
                new_state = current_state[:]
                new_state[zero_pos], new_state[new_pos] = new_state[new_pos], new_state[zero_pos]
                if tuple(new_state) not in visited:
                    visited.add(tuple(new_state))
                    open_set.put((len(path) + 1 + total_manhattan_distance(new_state), new_state, path + [new_state]))

    return None

# Solve the puzzle
solution = solve_puzzle(initial_state)

if solution:
    for i, state in enumerate(solution):
        print(f"Step {i + 1}:")
        for row in range(0, 9, 3):
            print(" ".join(map(str, state[row:row + 3])))

