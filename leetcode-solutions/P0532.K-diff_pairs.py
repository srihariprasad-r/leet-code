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

# Method 2
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        st = set()
        cnt = 0

        nums.sort()

        def bs(idx, x):
            l = 0
            r = len(nums) - 1

            while l <= r:
                mid = l + (r-l)//2

                if nums[mid] == x: return True if mid != idx else False

                if nums[mid] < x:
                    l = mid + 1
                else:
                    r = mid - 1

            return False

        for i in range(len(nums)):
            res1 = bs(i, nums[i]+k) 
            res2 = bs(i, nums[i]-k)
            if res1:
                o = (nums[i], nums[i]+k)  
            elif res2:
                o = (nums[i]-k, nums[i])
            if ((res1 or res2) and (o not in st)):
                cnt += 1
                st.add(o)

        return cnt