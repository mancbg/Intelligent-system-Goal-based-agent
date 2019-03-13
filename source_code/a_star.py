from node import *
from problem import *
import math
import heapq
import random

NODES_COUNT = 0


def a_star(problem, h=None):
    """
    A star algorithm
    :param problem: problem instance
    :param h: heuristic function name
    :return: solution path and number of nodes explored
    """
    global NODES_COUNT
    NODES_COUNT = 0
    return best_first_search(problem, lambda n: n.path_cost + h(n, problem.goal))


def best_first_search(problem, f):
    """
    Best First Search algorithm
    :param problem:
    :param f: total cost from source to destination = path cost + heuristic estimate
    :return: solution path and number of nodes explored
    """
    global NODES_COUNT
    node = Node(problem.initial_state)
    frontier = PriorityQueue(f)
    explored = set()
    frontier.append(node)
    while len(frontier) > 0:
        node = frontier.get()
        explored.add(repr(node.state))
        if problem.goal_test(node.state):
            print("Solution was reached in {} steps".format(node.depth + 1))
            return solution(node), NODES_COUNT
        else:
            for action in problem.actions(node.state):
                NODES_COUNT += 1
                child = child_node(problem, node, action)
                if repr(child.state) not in explored:
                    if child in frontier:  # have to check if it works. line 48
                        frontier_node = frontier[child]
                        if f(frontier_node) > f(child):
                            frontier.remove(frontier_node)
                            frontier.append(child)
                    else:
                        frontier.append(child)
    return 'failure', NODES_COUNT


def heuristic_1(node=None, goal=None):
    """
    Heuristic 1: h(n) = 0 for all nodes
    :param node: node n
    :param goal: goal attributes
    :return: h(n)
    """
    return 0


def heuristic_2(node=None, goal=None):
    """
    Heuristic 2: h(n) = random number
    :param node: node n
    :param goal: goal attributes
    :return: h(n)
    """
    return random.randint(0, 999)


def heuristic_3(node, goal):
    """
    Heuristic 3: manhattan distance betw node and goal
    :param node: node n
    :param goal: goal attr.
    :return: h(n)
    """
    return abs(goal[0] - node.state.current_row) + abs(goal[1] - node.state.current_column)


def heuristic_4(node, goal):
    """
    Heuristic 4: straight line distance between node and goal
    :param node: node n
    :param goal: goal
    :return: h(n)
    """
    return math.sqrt((goal[0] - node.state.current_row) ** 2 + (goal[1] - node.state.current_column) ** 2)


class PriorityQueue:
    """
    Implementation of Priority Queue
    """

    def __init__(self, f=lambda g: g):
        self.heap = []
        heapq.heapify(self.heap)
        self.f = f

    def append(self, node):
        heapq.heappush(self.heap, (self.f(node), node))

    def get(self):
        return heapq.heappop(self.heap)[1]

    def remove(self, node):
        for h in self.heap:
            if h[1] == node:
                self.heap.remove((h[0], node))
                heapq.heapify(self.heap)

    def __contains__(self, node):
        for h in self.heap:
            if h[1] == node:
                return True
        return False

    def __getitem__(self, node):
        for h in self.heap:
            if h[1] == node:
                return h[1]

    def __len__(self):
        return len(self.heap)
