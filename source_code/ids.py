import itertools
from node import *

NODES_COUNT = 0


def ids(problem):
    """
    Iterative Deepening Search algorithm implementation
    :param problem:
    :return: solution path and node explored count
    """
    global NODES_COUNT
    NODES_COUNT = 0
    # for depth in range(17, 30):
    for depth in itertools.count():
        print("Depth :{}".format(depth))
        result = dls(problem, depth)
        if result != 'cutoff':
            return result, NODES_COUNT


def dls(problem, limit):
    """
    Depth limited search
    :param problem: problem
    :param limit: depth limit
    :return: solution path and node explored count
    """
    return recursive_dls(make_node(problem.initial_state), problem, limit)


def recursive_dls(node, problem, limit):
    """
    Recursive depth limited search
    :param node: current node
    :param problem: problem
    :param limit: depth limit to be searched
    :return: solution path and node explored count
    """
    global NODES_COUNT
    if problem.goal_test(node.state):
        print("Solution was reached in {} steps".format(node.depth + 1))
        return solution(node)
    elif limit == 0:
        return 'cutoff'
    else:
        cutoff_flag = False
        for action in problem.actions(node.state):
            NODES_COUNT += 1
            child = child_node(problem, node, action)
            result = recursive_dls(child, problem, limit - 1)
            if result == 'cutoff':
                cutoff_flag = True
            elif result != 'failure':
                return result
        if cutoff_flag:
            return 'cutoff'
        else:
            return 'failure'
