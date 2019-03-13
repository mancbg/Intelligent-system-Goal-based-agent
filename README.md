# Intelligent system : Goal Based Agent
Implementation of a kind of goal based agent: Problem solving agent. 

The program has two types of searches implemented: Uninformed (IDS) and Informed (A*) search. A-star search has four different heuristics: two good and two not-so-good heuristics to analyze how a good heuristic can give better results.

Two problems formulated are: Maze solver (Problem.py) and N-queeens Game (nqueens.py). For maze solver, Program analyzes how one search algorithm (IDS) is not adequate, whereas the other search algorithm(A-star) gives us the best result. Any search problem formulated within these five terms: Initial state, Actions, Result/Transition Function, Goal test, Path cost, will be solved by this Problem Solving Agent (Provided Informed or Uninformed Search algorithm is adequate to solve the problem).

## How to begin
Two problems formulated are, Maze solver (Problem.py) and N-queeens Game (nqueens.py).

**Maze Solver**

Given a maze of 0s representing obstacles and 1s representing path, the program finds the shortest path (with A star search) and a path (not necessarily shortest, with IDS) from top left corner to right bottom corner.

- File to run: Problem.py
- sys arguments: input maze file of format .txt (check sample inputs)

**N Queens Problem**

Given n-queens problem where number of queens is specified by the user, the program finds the solution.
What is the N-queens problem: https://en.wikipedia.org/wiki/Eight_queens_puzzle

- File to run: nqueens.py
- Sys argument: Number of queens to be placed on the board

