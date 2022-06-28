from TreeNode import TreeNode

class RecursiveTraversal:
    def __init__(self):
        self.root = self._createTree()

    def _createTree(self):
        left = TreeNode(2)
        left.left = TreeNode(3)
        left.right = TreeNode(4)
        right = TreeNode(5)
        right.left = TreeNode(6)
        right.right = TreeNode(7)
        root = TreeNode(1, left, right)
        return root

    def preorderTraversal(self, root):
        sum = 0
        if not root:
            return sum
        sum += root.val
        sum += self.preorderTraversal(root.left)
        sum += self.preorderTraversal(root.right)
        return sum
    
    def inorderTraversal(self, root):
        sum = 0
        if not root:
            return sum
        sum += self.inorderTraversal(root.left)
        sum += root.val
        sum += self.inorderTraversal(root.right)
        return sum
    
    def postorderTraversal(self, root):
        sum = 0
        if not root:
            return sum
        sum += self.postorderTraversal(root.left)
        sum += self.postorderTraversal(root.right)
        sum += root.val
        return sum
    

rt = RecursiveTraversal()
print(rt.preorderTraversal(rt.root))
print(rt.inorderTraversal(rt.root))
print(rt.postorderTraversal(rt.root))
