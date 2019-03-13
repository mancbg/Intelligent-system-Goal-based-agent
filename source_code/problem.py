__author__ = 'MBG'

"""
CSCI-630 Project 1
Author: Manasi Bharat Gund

code for class Problem and class MazeState.
Other functions related to parsing the maze, and creating a Problem instance.

"""
from ids import *
from a_star import *
import copy
import sys
from turtle_maze import *


class Problem:
    """
    This class defines the maze problem
    """

    def __init__(self, initial_state, maze, goal=None):
        self.initial_state = initial_state
        self.maze = maze
        self.action_list = [self.go_up, self.go_right, self.go_down, self.go_left]
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

        # If it is possible to go up, add that action in the list
        if state.current_row > 0 and self.maze[state.current_row - 1][
            state.current_column] == '0' and not state.is_visited(state.current_row - 1, state.current_column):
            state_actions.append(self.action_list[0])

        # If it is possible to go right, add that action in the list
        if state.current_column < len(self.maze[0]) - 1 and self.maze[state.current_row][
            state.current_column + 1] == '0' and not state.is_visited(state.current_row, state.current_column + 1):
            state_actions.append(self.action_list[1])

        # If it is possible to go down, add that action in the list
        if state.current_row < len(self.maze) - 1 and self.maze[state.current_row + 1][
            state.current_column] == '0' and not state.is_visited(state.current_row + 1, state.current_column):
            state_actions.append(self.action_list[2])

        # If it is possible to go left, add that action in the list
        if state.current_column > 0 and self.maze[state.current_row][
            state.current_column - 1] == '0' and not state.is_visited(state.current_row, state.current_column - 1):
            state_actions.append(self.action_list[3])
        return state_actions

    def result(self, state, action):
        """
        Transition function : Calculates the next state from the current state, and the action
        :param state: Current state
        :param action: Action function to call
        :return: State resulting from the state and the action provided
        """
        new_state = action(state)
        return new_state

    def go_up(self, state):
        """
        Move one square up
        :param state: current state
        :return: Resulting state
        """
        # visited = copy.deepcopy(state.visited)
        # visited.append(state)
        return MazeState(state.current_row - 1, state.current_column)

    def go_right(self, state):
        """
        Move one square right
        :param state: current state
        :return: Resulting state
        """
        # visited = copy.deepcopy(state.visited)
        # visited.append((state.current_column, state.current_row))
        return MazeState(state.current_row, state.current_column + 1)

    def go_down(self, state):
        """
        Move one square down
        :param state: current state
        :return: resulting state
        """
        # visited = copy.deepcopy(state.visited)
        # visited.append((state.current_column, state.current_row))
        return MazeState(state.current_row + 1, state.current_column)

    def go_left(self, state):
        """
        Move one square left
        :param state: current state
        :return: resulting state
        """
        # visited = copy.deepcopy(state.visited)
        # visited.append((state.current_column, state.current_row))
        return MazeState(state.current_row, state.current_column - 1)

    def goal_test(self, state):
        """
        Check if the goal is reached
        :param state: current state
        :return: true, if the goal reached. False, otherwise
        """
        return self.goal[0] == state.current_row and self.goal[1] == state.current_column

    def show_path(self, path):
        """
        Given the list of states from the starting point to exit, print the path.
        :param path: list of states from initial to the state we reach the goal
        :return: the maze with path taken marked with Xs.
        """
        if type(path) is list:
            solution = copy.deepcopy(self.maze)
            for p in path:
                solution[p.current_row][p.current_column] = 'X'
            for row in solution:
                print(row)
            return solution
        else:
            print("No solution")
            return None


class MazeState:
    """
    This class creates instances for the different states the maze can be in
    """

    def __init__(self, current_row, current_column, visited=[]):
        self.visited = visited
        self.current_row = current_row
        self.current_column = current_column

    def __repr__(self):
        return '({}, {})'.format(self.current_row, self.current_column)

    def __eq__(self, other):
        return repr(self) == repr(other)

    def is_visited(self, row, column):
        """
        Check if row, column is in visited or not.
        :param row: row
        :param column: column
        :return: true if in visited, otherwise false.
        """
        return (row, column) in self.visited


def formulate_maze_problem(file):
    """
    Formulate the maze problem from the text file
    :param file: .txt
    :return: instance of Problem class
    """
    maze = parse_file(file)

    # Set starting point
    start_row, start_column = set_starting_point(maze)

    # If starting point is an obstacle, return None
    if start_row is None and start_column is None:
        return None

    # Mark the starting point as X. Not compulsory.
    maze[start_row][start_column] = 'X'

    # Set the goal coordinates
    goal_row, goal_column = set_goal(maze)

    # If goal coordinates has an obstacle, return None
    if goal_row is None and goal_column is None:
        return None

    # Maze as a Problem instance
    problem = Problem(MazeState(start_row, start_column), maze, [goal_row, goal_column])
    return problem


def parse_file(file):
    """
    Parse the input maze in a list of list
    :param file: .txt
    :return: maze list
    """
    with open(file, "r") as file:
        parsed_list = [line.strip().split() for line in file.readlines()]
    return parsed_list


def set_starting_point(maze):
    """
    Set starting point as (0,0)
    :param maze: problem maze
    :return: 0,0 if success, else None.
    """
    row, column = None, None
    if maze[0][0] == '0':
        row, column = 0, 0
    return row, column


def set_goal(maze):
    """
    Set goal coordinates as (last row, last column)
    :param maze: problem maze
    :return: coordinates of goal, if success. Else None.
    """
    row, column = None, None
    if maze[len(maze) - 1][len(maze[0]) - 1] == '0':
        row, column = len(maze) - 1, len(maze[0]) - 1
    return row, column


def main(argv):
    # Formulate the problem as a Problem instance
    print("Please pass the input maze file as command line argument")
    problem = formulate_maze_problem(argv[1])

    # If the problem is successfully defined, proceed.
    if problem:

        # Using various search algorithms on the problem

        # print("\nA* search with Heuristic 1: h(n) = 0")
        # path1, nodes_count1 = a_star(problem, heuristic_1)
        # if path1 and nodes_count1:
        #     # Effective branching factor calculation
        #     print("No of nodes generated : ", nodes_count1)
        #     print("Effective branching factor is : ", math.exp(math.log(nodes_count1) / len(path1)))
        #
        # print("\nA* search with Heuristic 2: Random num from 0 till 999")
        # path2, nodes_count2 = a_star(problem, heuristic_2)
        # if path2 and nodes_count2:
        #     # Effective branching factor calculation
        #     print("No of nodes generated : ", nodes_count2)
        #     print("Effective branching factor is : ", math.exp(math.log(nodes_count2) / len(path2)))
        #
        # print("\nA* search with Heuristic 3: Manhattan distance")
        # path3, nodes_count3 = a_star(problem, heuristic_3)
        # if path3 and nodes_count3:
        #     # Effective branching factor calculation
        #     print("No of nodes generated : ", nodes_count3)
        #     print("Effective branching factor is : ", math.exp(math.log(nodes_count3) / len(path3)))

        print("\nA* search with Heuristic 4: Euclidean distance")
        path4, nodes_count4 = a_star(problem, heuristic_4)
        if path4 and nodes_count4:
            # Effective branching factor calculation
            print("No of nodes generated : ", nodes_count4)
            print("Effective branching factor is : ", math.exp(math.log(nodes_count4) / len(path4)))

        # Print the solution, currently using A* heuristic 4 result
        print("Path with A* heuristic 4 result is shown in turtle. Uncomment for other algorithms paths on turtle.")
        solution4 = problem.show_path(path4)
        if solution4:
            # Draw the maze with turtle, currently using Heuristic 4 result
            draw_maze(solution4)

        # Commented part for other algorithms

        # solution1 = problem.show_path(path1)
        # if solution1:
        # Draw the maze with turtle, currently using Heuristic 1 result
        # draw_maze(solution1)

        # solution2 = problem.show_path(path2)
        # if solution2:
        # Draw the maze with turtle, currently using Heuristic 2 result
        # draw_maze(solution2)

        # solution3 = problem.show_path(path3)
        # if solution3:
        # Draw the maze with turtle, currently using Heuristic 3 result
        # draw_maze(solution4)

        print("\nUncomment IDS to see the result")
        # print("IDS - Depth currently on is displayed for reference")
        # path_ids, nodes_count_ids = ids(problem)

        # if path_ids and nodes_count_ids:
        #     # Effective branching factor calculation
        #     print("No of nodes generated : ", nodes_count_ids)
        #     print("Effective branching factor is : ", math.exp(math.log(nodes_count_ids) / len(path_ids)))

    else:
        print('No Solution')


if __name__ == '__main__':
    main(sys.argv)
