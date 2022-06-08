class Solution(object):
    def longestMountain(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        ans = left = right = 0
        n = len(arr)

        while left < n:
            while left < n - 1 and arr[left] >= arr[left+1]:
                left += 1

            right = left + 1
            while right < n - 1 and arr[right] < arr[right+1]:
                right += 1

            while right < n - 1 and arr[right] > arr[right+1]:
                right += 1
                ans = max(ans, right-left+1)

            left = right

        return ans