from collections import deque


def safe(m_left, c_left, total_m, total_c):
    m_right = total_m - m_left
    c_right = total_c - c_left

    if m_left < 0 or c_left < 0:
        return False

    if m_right < 0 or c_right < 0:
        return False

    if m_left > 0 and c_left > m_left:
        return False

    if m_right > 0 and c_right > m_right:
        return False

    return True


def missionaries_cannibals(total_m, total_c):
    start = (total_m, total_c, 0)
    goal = (0, 0, 1)

    queue = deque([(start, [])])
    visited = set()

    moves = [
        (1, 0),
        (2, 0),
        (0, 1),
        (0, 2),
        (1, 1)
    ]

    while queue:
        state, path = queue.popleft()

        if state in visited:
            continue

        visited.add(state)
        path = path + [state]

        m_left, c_left, boat = state

        if state == goal:
            print("\nSolution found!")

            for i, (m, c, b) in enumerate(path):
                m_right = total_m - m
                c_right = total_c - c

                side = "Left" if b == 0 else "Right"

                print(
                    f"Step {i}: "
                    f"Left = ({m}M, {c}C), "
                    f"Right = ({m_right}M, {c_right}C), "
                    f"Boat = {side}"
                )

            return

        for m, c in moves:

            if m + c == 0 or m + c > 2:
                continue

            if boat == 0:
                new_state = (
                    m_left - m,
                    c_left - c,
                    1
                )
            else:
                new_state = (
                    m_left + m,
                    c_left + c,
                    0
                )

            if new_state in visited:
                continue

            if safe(
                new_state[0],
                new_state[1],
                total_m,
                total_c
            ):
                queue.append((new_state, path))

    print("No solution found.")


m = int(input("Enter number of missionaries: "))
c = int(input("Enter number of cannibals: "))

if m <= 0 or c <= 0:
    print("Numbers must be positive.")

elif m != c:
    print("This program is designed for equal numbers.")

else:
    missionaries_cannibals(m, c)