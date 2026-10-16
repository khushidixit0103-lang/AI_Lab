from collections import deque

def water_jug(a_capacity, b_capacity, target):

    queue = deque([(0, 0, [])])
    visited = set()

    while queue:
        a, b, path = queue.popleft()

        if (a, b) in visited:
            continue

        visited.add((a, b))
        path = path + [(a, b)]

        if a == target or b == target:
            print("\nSolution found!")
            for i, state in enumerate(path):
                print(f"Step {i}: Jug A = {state[0]} L, Jug B = {state[1]} L")
            return

        next_states = [
            (a_capacity, b),  # Fill Jug A
            (a, b_capacity),  # Fill Jug B
            (0, b),           # Empty Jug A
            (a, 0),           # Empty Jug B
            (a - min(a, b_capacity - b),
             b + min(a, b_capacity - b)),  # Pour A into B
            (a + min(b, a_capacity - a),
             b - min(b, a_capacity - a))   # Pour B into A
        ]

        for state in next_states:
            if state not in visited:
                queue.append((state[0], state[1], path))

    print("Target cannot be measured with these jug capacities.")


a_capacity = int(input("Enter capacity of Jug A: "))
b_capacity = int(input("Enter capacity of Jug B: "))
target = int(input("Enter target amount: "))

if a_capacity <= 0 or b_capacity <= 0:
    print("Jug capacities must be positive.")
elif target < 0 or target > max(a_capacity, b_capacity):
    print("Invalid target amount.")
else:
    water_jug(a_capacity, b_capacity, target)