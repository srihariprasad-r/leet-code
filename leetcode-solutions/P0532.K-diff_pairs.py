class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()

        lst = []

        cnt = 0

        def ok(arr, low, target):
            high = len(arr) - 1
            while low <= high:
                mid = low + (high-low)//2
                if nums[mid] == target:
                    return True
                if nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1

            return False

        for i in range(len(nums)):
            if i > 0 and nums[i] - nums[i-1] == 0:
                continue

            if ok(nums, i + 1, nums[i] + k):
                cnt += 1

        return cnt

# Method 2 - wrong submission
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        cnt = 0
        st = set()

        def bs(idx, tgt, n):
            l = 0
            r = len(nums)-1

            while l <= r:
                mid = l + (r-l+1)//2

                if abs(tgt-n) == nums[mid]: return mid if mid != idx else -1

                if abs(tgt - n) < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

            return -1

        for i in range(len(nums)-1, -1, -1):
            if ((nums[i], abs(k-nums[i])) not in st or not(i > 0 and nums[i] == nums[i-1])):
                res = bs(i, k, nums[i])
                if 0 <= res < len(nums):
                    st.add((nums[i], abs(k-nums[i])))
                    cnt += 1

        return cnt