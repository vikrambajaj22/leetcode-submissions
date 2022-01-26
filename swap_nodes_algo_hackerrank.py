#!/bin/python3

import sys
# for last 2 test cases to work without exceeding recursion depth
sys.setrecursionlimit(15000)


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def create_tree(root, indexes):
    queue = [root]
    for l, r in indexes:
        node = queue.pop(0)
        if l != -1:
            node.left = TreeNode(val=l)
            queue.append(node.left)
        if r != -1:
            node.right = TreeNode(val=r)
            queue.append(node.right)
    return root


def performSwap(root, k, level, traversal):
    if root:
        if level % k == 0:
            root.left, root.right = root.right, root.left

        performSwap(root.left, k, level+1, traversal)
        traversal.append(root.val)
        performSwap(root.right, k, level+1, traversal)


def swapNodes(indexes, queries):
    root = TreeNode(val=1)
    root = create_tree(root, indexes)

    result = []  # will store results after each query as inorder traversal

    for k in queries:
        traversal = []
        level = 1
        performSwap(root, k, level, traversal)
        result.append(traversal)

    return result


if __name__ == '__main__':
    # indexes contains nodes in level-order, each tuple containing (l, r) children, -1 indicates no child
    # root is 1 by default
    indexes = [(2, 3), (4, -1), (5, -1), (6, -1), (7, 8), (-1, 9),
               (-1, -1), (10, 11), (-1, -1), (-1, -1), (-1, -1)]

    # the above tree would look as follows
    #            1
    #          /    \
    #         2      3
    #       /       /
    #      4       5
    #     /       / \
    #    6       7   8
    #     \         / \
    #      9       10  11

    # first swap children of every 2nd level and then swap children of every 4th level (levels start at 1)
    queries = [2, 4]

    # [[2, 9, 6, 4, 1, 3, 7, 5, 11, 8, 10], [2, 6, 9, 4, 1, 3, 7, 5, 10, 8, 11]]
    print(swapNodes(indexes, queries))
