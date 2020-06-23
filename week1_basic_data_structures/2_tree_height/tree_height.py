# python3

import sys
import threading
import random

class Tree:
    def __init__(self, val=0):
        self.val = val
        self.child = [None]
    def __repr__(self):
        return f'Tree val: {self.val} child: {self.child}'

    def addChild(self, node):
        self.child.append(node)


def create_tree(n, parents):
    # Replace this code with a faster implementation
    nodes = [Tree(i) for i in range(n)]
    for childnode in range(n):
        parent = parents[childnode]
        if parent == -1:
            root = nodes[childnode]
        else:
            nodes[parent].addChild(nodes[childnode])
    nodes = []
    return root

def compute_height(root):
    if not root:
        return 0
    children = []
    for node in root.child:
        children.append(compute_height(node))
    return 1 + max(children)


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    # n = random.randrange(1, 30)
    # root_index = random.randrange(0, n)
    # parents = [random.randrange(0, n) for _ in range(root_index)] + [-1] + [random.randrange(0, n) for _ in range(root_index + 1, n)]
    print(compute_height(create_tree(n, parents)))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
