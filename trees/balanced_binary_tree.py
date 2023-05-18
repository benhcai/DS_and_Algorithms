def depth(node):
    if node == None:
        return 0
    leftDepth = depth(node.left)
    rightDepth = depth(node.right)
    maxDepth = max(leftDepth, rightDepth) + 1
    return maxDepth

def isBalanced(node):
    if node == None:
        return True

    left = depth(node.left)
    right = depth(node.right)

    return abs(left-right) <= 1

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

a = Node(0)

b = Node(1)
c = Node(2)
d = Node(4)

a.left = b
b.left = c
c.left = d

e = Node(5)
f = Node(6)
g = Node(7)

a.right = e
# e.right = f
# f.right = g

print(isBalanced(a))
