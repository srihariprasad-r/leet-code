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

# Method 2 - Code issue exists


class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def merge(left, mid, right, arr, tmp, res):
            i = left
            j = mid
            k = 0
            cnt = 0

            while i < mid and j <= right:
                if arr[i] <= arr[j]:
                    tmp[k] = arr[i]
                    i += 1
                    k += 1
                else:
                    tmp[k] = arr[j]
                    cnt += 1
                    res[j-i] = cnt
                    j += 1
                    k += 1

            while i < mid:
                tmp[k] = arr[i]
                i += 1
                k += 1
            while j <= right:
                tmp[k] = arr[j]
                j += 1
                k += 1

            for m in range(left, right):
                arr[m] = tmp[m]

            return

        def mergesort(left, right, arr, tmp, res=[]):
            mid = 0
            cnt = 0
            if right > left:
                mid = (right + left) / 2
                mergesort(left, mid, arr, tmp, res)
                mergesort(mid+1, right, arr, tmp, res)
                merge(left, mid+1, right, arr, tmp, res)

            return res[::-1]

        return mergesort(0, len(nums)-1, nums, [-1]*len(nums), [0]*len(nums))
