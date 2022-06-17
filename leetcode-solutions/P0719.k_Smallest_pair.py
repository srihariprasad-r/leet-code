#wrong submission

class Solution(object):
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        arr = []

        for i in range(len(nums)):
            j = i + 1
            while j < len(nums):
                arr.append(abs(nums[i]-nums[j]))
                j += 1

        heapq.heapify(arr)

        return arr[k-1]
