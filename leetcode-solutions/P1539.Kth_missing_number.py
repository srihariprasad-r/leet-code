class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        l = 0
        r = len(arr) - 1

        while l <= r:
            mid = l + (r-l+1)//2

            missing = arr[mid] - (mid+1)
            if missing < k:
                l = mid + 1
            else:
                r = mid - 1

        return l + k