# TLE

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1: return nums
        def merge(arr, l, mid, r):
            # changed from len(arr) -> r - l + 1 to fix TLE
            tmp = [0] * (r - l + 1)

            k = 0
            low = l
            high = mid + 1
            while low <= mid and high <= r:
                if arr[low] >= arr[high]:
                    tmp[k] = arr[high]
                    high += 1
                    k += 1
                else:
                    tmp[k] = arr[low]
                    k += 1
                    low += 1

            while low <= mid:
                tmp[k] = arr[low]
                k += 1
                low += 1

            while high <= r:
                tmp[k] = arr[high]
                k += 1   
                high += 1     

            for i in range(l, r+1):
                arr[i] = tmp[i-l]

            return arr
        
        def mergesort(arr, l, r):
            if l == r: return
            mid = (l + r)// 2
            mergesort(arr, l, mid)
            mergesort(arr, mid+1, r)
            merge(arr, l, mid, r)

            return arr

        return mergesort(nums, 0, len(nums)-1)
