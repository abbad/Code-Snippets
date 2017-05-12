from sys import maxint
from copy import copy

__author__ = 'Abbad'

def dijkstra(network, start, end):
    """
    You can make this code with priorityDict http://code.activestate.com/recipes/117228/
    :param network: a dictionary {'name_of_train_station': list of adjacent nodes represented as a dictionary }
    :param start: starting node
    :param end: ending node
    :return: tuple of cost and path.
    """
    # sanity check
    if start == end:
        return [start], 0
    if start not in network:
        return []

    # This is defensive programming.
    if end not in network:
        raise Exception("There is no terminal node called ")

    labels = dict()  # used for distances calculated while finding the shortest path.

    # record whether a label was updated
    order = dict()

    # Mark all nodes as unreachable. Except the start one.
    for node in network.keys():
        if node == start:
            labels[node] = 0  # shortest distance form start to itself is zero.
        else:
            labels[node] = maxint  # initial labels are infinity

    unseen_nodes = copy(labels)

    # Begin algorithm
    while len(unseen_nodes) > 0:
        # Get the minimum adjacent value.
        min_node = min(unseen_nodes, key=unseen_nodes.get)  # min_node is the node with the smallest label
        # Loop over them and try to figure out which one is the lowest.
        for i in network[min_node]:
            if labels[i] > (labels[min_node] + network[min_node][i]):
                labels[i] = labels[min_node] + network[min_node][i]
                unseen_nodes[i] = labels[min_node] + network[min_node][i]
                order[i] = min_node
        # Once we discover the node we just delete it from the unseen node.
        del unseen_nodes[min_node]

    # Rearrange and prepare the output.
    temp = copy(end)
    path = []

    while temp != start:
        path.append(temp)
        temp = order[temp]

    path.append(start)
    path.reverse()

    if not labels[end]:
        return path, None
    return path, labels[end]