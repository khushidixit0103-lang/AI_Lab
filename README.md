🪣 Water Jug Problem Using Python

📌 About the Project

The Water Jug Problem is a classic Artificial Intelligence problem. The objective is to measure a specific amount of water using two jugs of different capacities.

This program uses Breadth-First Search (BFS) to find a solution and displays each step with the amount of water in both jugs.

🎯 Objectives

- Take jug capacities and the target amount as user input.
- Explore possible states of the two jugs.
- Find a solution using BFS.
- Display each step of the solution.

🛠️ Technologies Used

- Python 3.14.8
- Visual Studio Code

⚙️ How the Program Works

The program represents each state as a pair:

"(Amount of water in Jug A, Amount of water in Jug B)"

It explores the following operations:

1. Fill Jug A.
2. Fill Jug B.
3. Empty Jug A.
4. Empty Jug B.
5. Pour water from Jug A into Jug B.
6. Pour water from Jug B into Jug A.

BFS explores the possible states using a queue until either jug contains the target amount. A visited set prevents the program from repeatedly exploring the same state.

▶️ How to Run the Program

1. Install Python on your computer.
2. Download or clone this repository.
3. Open the project folder in VS Code.
4. Open the terminal.
5. Run the following command:

python water_jug.py

6. Enter the capacities of both jugs and the target amount when prompted.

💻 Sample Input

Enter capacity of Jug A: 4
Enter capacity of Jug B: 3
Enter target amount: 2

📤 Sample Output

Solution found!
Step 0: Jug A = 0 L, Jug B = 0 L
Step 1: Jug A = 0 L, Jug B = 3 L
Step 2: Jug A = 3 L, Jug B = 0 L
Step 3: Jug A = 3 L, Jug B = 3 L
Step 4: Jug A = 4 L, Jug B = 2 L

Result: The target amount of 2 litres is achieved in Jug B.

🧠 Algorithm Used

Breadth-First Search (BFS)

BFS explores states level by level using a queue. It finds a solution with the fewest operations when each operation has equal cost.

📚 Concepts Learned

- Artificial Intelligence problem-solving
- State-space representation
- Breadth-First Search
- Queues and sets in Python
- User input and output

👩‍💻 Author

Created as part of an AI Lab practical assignment.
