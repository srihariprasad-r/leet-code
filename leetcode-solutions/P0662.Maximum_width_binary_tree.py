# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue = collections.deque()

        queue.append(([root, 0]))
        result = 0

        while queue:
            result = max(result, queue[-1][1] - queue[0][1] + 1)

            for _ in range(len(queue)):
                node, idx = queue.popleft()
                if node.left:
                    queue.append((node.left, idx * 2))

                if node.right:
                    queue.append((node.right, idx*2+1))

        return result
