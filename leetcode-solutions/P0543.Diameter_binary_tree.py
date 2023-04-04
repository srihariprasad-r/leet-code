class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = float('-inf')

        def traverse(node):
            if not node:
                return 0

            left = 0
            right = 0

            if node.left:
                left = traverse(node.left)

            if node.right:
                right = traverse(node.right)

            diameter = left + right
            self.res = max(self.res, diameter)

            return 1 + max(left, right)

        traverse(root)

        return self.res
