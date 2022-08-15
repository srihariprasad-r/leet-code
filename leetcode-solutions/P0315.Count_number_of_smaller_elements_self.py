# wrong submission

class Node:
    def __init__(self, val):
        self.val = val
        self.count = 0
        self.smallercnt = 0
        self.left = None
        self.right = None


class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = [0] * len(nums)

        def add(nums):
            node = root
            tsum = 0

            while node.val != nums:
                if node.val > nums:
                    if not node.left:
                        node.left = Node(nums)

                    node.smallercnt += 1
                    node = node.left
                else:
                    tsum += node.smallercnt + node.count
                    if not node.right:
                        node.right = Node(nums)

                    # node.smallercnt += 1
                    node = node.right

            node.count += 1

            return tsum + node.smallercnt

        root = Node(nums[-1])
        for i in range(len(nums)-1, -1, -1):
            ans[i] = add(nums[i])

        return ans
