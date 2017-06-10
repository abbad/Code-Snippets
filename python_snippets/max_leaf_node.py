# Find the sum of all left leaves in a given binary tree.
# Example:
#    3
#    / \
#   9  20
#     /  \
#    15   7
#
# 1
#      2  3
#    4  5
#
# There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.


class Node(object):

    def __init__(self, right, left, val):
        self.right = right
        self.left = left
        self.val = val

    def __repr__(self):
        return '%r' % self.val


def get_left_leaf_sum(node, acc_sum):

    if not node:
        return acc_sum

    if node.left and not node.left.left and not node.left.right:
        acc_sum += node.left.val + get_left_leaf_sum(node.right, acc_sum)
    else:
        return get_left_leaf_sum(node.right, acc_sum) + get_left_leaf_sum(node.left, acc_sum)
    return acc_sum


if __name__ == '__main__':
    node_15 = Node(None, None, 15)
    node_7 = Node(None, None, 7)
    node_20 = Node(node_7, node_15, 20)
    node_9 = Node(None, None, 9)
    node_3 = Node(node_20, node_9, 3)

    print(get_left_leaf_sum(node_3, 0))