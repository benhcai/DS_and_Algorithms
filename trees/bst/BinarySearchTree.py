from Node import Node

class BinarySearchTree:
    def __init__(self, val=0, left=None, right=None):
        self.root = Node(val, left, right)

    def insert(self, val):
        if not self.root:
            self.root = Node(val)
            return self.root
        current = self.root
        parent = None
        while current:
            parent = current
            if val < current.val:
                current = current.left
            else:
                current = current.right

        if (val < parent.val):
            parent.left = Node(val)
        else:
            parent.right = Node(val)

    def insert_rec(self, val):
        if val < self.root.val:
            if self.root.left:
                self.root.left.insert_rec(val)
            else:
                self.root.left = Node(val)
                return
        else:
            if self.root.right:
                self.root.right.insert_rec(val)
            else:
                self.root.right = Node(val)
                return
    
    def display(self, node=None):
        node = node or self.root
        lines, _, _, _ = self._display_aux(node)
        for line in lines:
            print(line)

    def _display_aux(self, node):
        # No child.
        if node.right is None and node.left is None:
            line = str(node.val)
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if node.right is None:
            lines, n, p, x = self._display_aux(node.left)
            s = str(node.val)
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            final_lines = [first_line, second_line] + shifted_lines
            return final_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if node.left is None:
            lines, n, p, x = self._display_aux(node.right)
            s = str(node.val)
            u = len(s)
    #        first_line = s + x * '_' + (n - x) * ' '
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            final_lines = [first_line, second_line] + shifted_lines
            return final_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self._display_aux(node.left)
        right, m, q, y = self._display_aux(node.right)
        s = '%s' % node.val
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * \
            '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + \
            (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + \
            [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2








