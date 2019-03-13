__author__ = 'MBG'

"""
CSCI-630 Project 1
Author: Manasi Bharat Gund

code for class NqProblem and class NqState.
Other functions related to parsing the input, and creating a Problem instance for N queens.

"""
from ids import *
from a_star import *
import copy
import sys
from turtle_maze import *


class NqProblem:
    """
    This class defines the n queens problem
    """

    def __init__(self, initial_state, board, size, goal=None):
        self.initial_state = initial_state
        self.board = board
        self.action_list = list()
        self.size = size
        for i in range(size):
            self.action_list.append(i)
        self.goal = goal

    def __repr__(self):
        return '{} -> {}'.format(self.initial_state, self.goal)

    def actions(self, state):
        """
        Calculate the list of possible actions from this particular state
        :param state: Current state
        :return: List of possible actions
        """
        state_actions = []
        if state.current_column + 1 < self.size:
            for i in range(self.size):
                if (i, state.current_column + 1) not in state.blocked:
                    state_actions.append(i)
        return state_actions

    def result(self, state, action):
        """
        Transition function : Calculates the next state from the current state, and the action
        :param state: Current state
        :param action: Action function to call
        :return: State resulting from the state and the action provided
        """
        new_blocked = copy.deepcopy(state.blocked)
        row = action
        column = state.current_column + 1
        for i in range(0, self.size):
            new_blocked.add((i, column))
            new_blocked.add((row, i))
            if 0 <= row + i <= self.size - 1 and 0 <= column + i <= self.size - 1:
                new_blocked.add((row + i, column + i))
            if 0 <= row - i <= self.size - 1 and 0 <= column - i <= self.size - 1:
                new_blocked.add((row - i, column - i))
            if 0 <= row + i <= self.size - 1 and 0 <= column - i <= self.size - 1:
                new_blocked.add((row + i, column - i))
            if 0 <= row - i <= self.size - 1 and 0 <= column + i <= self.size - 1:
                new_blocked.add((row - i, column + i))

        new_state = NqState(row, column, new_blocked)
        self.action_list[i] = 1
        return new_state

    def goal_test(self, state):
        """
        Check if the goal is reached
        :param state: current state
        :return: true, if the goal reached. False, otherwise
        """
        return self.goal == state.current_column

    def show_path(self, path):
        """
        Given the list of states from the starting point to exit, print the path.
        :param path: list of states from initial to the state we reach the goal
        :return: the maze with path taken marked with Xs.
        """
        if type(path) is list:
            solution = copy.deepcopy(self.board)
            for p in path[1:]:
                solution[p.current_row][p.current_column] = "X"
            for row in solution:
                print(row)
            return solution
        else:
            print("No solution")
            return None


class NqState:
    """
    This class creates instances for the different states the maze can be in
    """

    def __init__(self, current_row, current_column, blocked=set([])):
        self.current_row = current_row
        self.current_column = current_column
        self.blocked = blocked

    def __repr__(self):
        return "{},{},{}".format(self.current_row, self.current_column, self.blocked)


def formulate_nqueens_problem(size):
    """
    Formulate the n queens problem from the size
    :param file: size positive integer
    :return: instance of NqProblem class
    """

    # Set initial state point
    initial_state = set_initial_state(size)

    board = list()
    for i in range(size):
        board.append(list())
        for j in range(size):
            board[i].append(0)

    # Set the goal coordinates
    goal = size - 1

    # Maze as a Problem instance
    problem = NqProblem(initial_state, board, size, goal)
    return problem


def set_initial_state(size):
    """
    Set initial state as -1,-1
    :param size: problem size by size
    """
    return NqState(-1, -1)


def main(argv):
    # Formulate the problem as a Problem instance
    print("Please pass the size of N-Queens puzzle as a command line argument")
    problem = formulate_nqueens_problem(int(argv[1]))

    # If the problem is successfully defined, proceed.
    if problem:

        print("\nA* search with Heuristic 1: h(n) = 0")
        path1, nodes_count1 = a_star(problem, heuristic_1)
        if path1:
            solution = problem.show_path(path1)
            draw_maze(solution)

    else:
        print('No Solution')


if __name__ == '__main__':
    main(sys.argv)
