| Name | ID | Section |
| :--- | :--- | :--- |
| Samuek Abraham| ugr/0041/16 | 02 |


# Maze Generator and Solver

This project is a visual maze generator and maze solver built using Python and Pygame.

The maze is generated using a **Depth-First Search (DFS)** algorithm with a **stack-based backtracking approach**, often compared to the behavior of a “mouse” exploring a maze. The algorithm starts from a random cell, moves to an unvisited neighboring cell, removes the wall between them, and pushes the current cell onto a stack. When the algorithm reaches a dead end, it backtracks by popping cells from the stack until it finds a new path to continue exploring.

This process continues until every cell in the grid has been visited, producing a perfect maze with one unique path between any two cells.

After generation, the maze is automatically solved using another DFS traversal. The solver visually demonstrates:
- The current exploration node (Red)
- The successful path (Green)
- Dead ends and backtracked paths (Blue)

## Features

- Random maze generation
- Stack-based DFS backtracking
- Real-time maze visualization
- Automatic maze solving
- Animated pathfinding process
- Dead-end visualization using colors

## Technologies Used

- Python
- Pygame

## Controls

- Close the window to exit the program.

## How It Works

### Maze Generation
1. Start from a random cell.
2. Mark the cell as visited.
3. Randomly choose an unvisited neighboring cell.
4. Remove the wall between the current and chosen cell.
5. Push the current cell onto a stack.
6. Move to the chosen neighbor.
7. If no unvisited neighbors exist, backtrack using the stack.
8. Repeat until all cells are visited.

### Maze Solving
The solver uses DFS again to search for a path from the entrance `(0,0)` to the exit `(R-1,C-1)` while visualizing:
- explored nodes,
- backtracking,
- and the final solution path.

## Installation

Install Pygame before running:

```bash
pip install pygame
```

## Run the Program

```bash
python Maze-CG.py
```
