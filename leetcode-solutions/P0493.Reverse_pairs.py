# TLE submission

class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = 0
        
        for i in range(len(nums)):
            j = i + 1

            while j < len(nums):
                if nums[i] > nums[j] * 2:
                    cnt += 1
                j += 1
            
        return cnt

# merge sort
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge(arr, l, mid, r):
            cnt = 0
            low = l
            high = mid + 1
            # moved here to fix TLE
            j = high
            for i in range(low, mid+1):
                while j <= r and arr[i] > 2 * nums[j]:
                    j += 1

                cnt += j - (mid+1)
            
            tmp = [0] * (r-l+1)
            k = 0
            while low <= mid and high <= r:
                if arr[low] >= arr[high]:
                    tmp[k] = arr[high]
                    high += 1
                    k += 1
                else:
                    tmp[k] = arr[low]
                    low += 1
                    k += 1

            while low <= mid:
                tmp[k] = arr[low]
                low += 1
                k += 1

            while high <= r:
                tmp[k] = arr[high]
                high += 1
                k += 1

            for i in range(l, r+1):
                arr[i] = tmp[i-l]

            return cnt

        def mergesort(arr, l, r):
            if l == r: return 0
            mid = (l + r) //2
            c = mergesort(arr, l, mid)
            c += mergesort(arr, mid+1, r)
            c += merge(arr, l, mid, r)

            return c

        return mergesort(nums, 0, len(nums)-1)
            
            