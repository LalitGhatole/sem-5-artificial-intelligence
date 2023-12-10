from collections import deque

def water_jug_problem():
    jug1_capacity = int(input("Enter the capacity of the first jug: "))
    jug2_capacity = int(input("Enter the capacity of the second jug: "))
    target_amount = int(input("Enter the target amount of water: "))

    visited = set()
    queue = deque([(0, 0, "Initial state: Both jugs are empty")])

    while queue:
        jug1_current, jug2_current, path = queue.popleft()
        if jug1_current == target_amount or jug2_current == target_amount:
            print(f"Target amount of water {target_amount} reached!")
            print(path)
            return

        if (jug1_current, jug2_current) in visited:
            continue
        visited.add((jug1_current, jug2_current))

        # Fill jug1
        queue.append((jug1_capacity, jug2_current, f"{path} -> Fill jug 1"))
        # Fill jug2
        queue.append((jug1_current, jug2_capacity, f"{path} -> Fill jug 2"))
        # Empty jug1
        queue.append((0, jug2_current, f"{path} -> Empty jug 1"))
        # Empty jug2
        queue.append((jug1_current, 0, f"{path} -> Empty jug 2"))
        # Pour jug1 to jug2
        pour_amount = min(jug1_current, jug2_capacity - jug2_current)
        queue.append((jug1_current - pour_amount, jug2_current + pour_amount, f"{path} -> Pour jug 1 to jug 2"))
        # Pour jug2 to jug1
        pour_amount = min(jug2_current, jug1_capacity - jug1_current)
        queue.append((jug1_current + pour_amount, jug2_current - pour_amount, f"{path} -> Pour jug 2 to jug 1"))

    print("Cannot reach the target amount of water.")

if __name__ == "__main__":
    water_jug_problem()
