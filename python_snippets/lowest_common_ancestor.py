"""
    Find the lowest common ancestor in a binary tree.
     a
    / \
   b   e
 /  \
c   d
"""


class Tree(object):
    """

    """
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left_child = left
        self.right_child = right

    def __repr__(self):
        return str(self.value)


def find_path(root, target, path):
    """
    Find the path to the target.
    :param root:
    :param target:
    :return:
    """
    # Base case.
    if root is None:
        return False

    path.append(root.value)

    if target.value == root.value:
        return True

    # Iterate over the tree.
    if (root.left_child and find_path(root.left_child, target, path)) or \
            (root.right_child and find_path(root.right_child, target, path)):
        return True

    path.pop()
    return False

def lowest_common_ancestor(tree, nodeA, nodeB):
    """
    A function to return lowest common ancestor.
    :param tree:
    :param nodeA:
    :param nodeB:
    :return: Lowest ancestor node.
    """
    pathA = []
    pathB = []

    # Starting from the root visit and mark until you reach either A or B. Do two stacks for it.
    if (not find_path(tree, nodeA, pathA)) or (not find_path(tree, nodeB, pathB)):
        return -1

    i = 0
    result = -1
    while pathA[i] and pathB[i]:
        if pathA[i] != pathB[i]:
            result = pathA[i - 1]
            break
        i += 1

    return result

if __name__ == '__main__':
    treeD = Tree('D')
    treeC = Tree('C')
    treeE = Tree('E')
    treeB = Tree('B', treeC, treeD)
    tree = Tree('A', treeB, treeE)

    assert lowest_common_ancestor(tree, treeC, treeD) == 'B'
