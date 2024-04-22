# wrong submission
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        ms_arr = [0] * (len(arr)+1)

        for idx, c in enumerate(arr):
            ms_arr[idx+1] = c - idx-1

        l = 1
        r = len(ms_arr) - 1

        while l < r:
            mid = l + (r-l+1)//2

            if ms_arr[mid] == k: return mid
            
            if ms_arr[mid] < k:
                l = mid + 1
            else:
                r = mid - 1

        if l == len(arr): return arr[l-1] + k

        return arr[l-1] + ms_arr[l] - 1