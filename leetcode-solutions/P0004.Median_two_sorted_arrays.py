class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = []
        s = 0
        i = 0
        j = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                arr.append(nums1[i])
                i += 1
            else:
                arr.append(nums2[j])
                j += 1

        while i < len(nums1):
            arr.append(nums1[i])
            i += 1

        while j < len(nums2):
            arr.append(nums2[j])
            j += 1

        if len(arr) % 2 == 0:
            s = (arr[len(arr)//2] + arr[(len(arr)//2) - 1]) / 2
        else:
            s = arr[len(arr)//2]

        return s

# Method 2
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        if n1 > n2: return self.findMedianSortedArrays(nums2, nums1) 
        n = n1 + n2
        low = 0 
        high = n1
        l = (n1+n2+1)//2
        while low <= high:
            mid = low + (high-low)//2
            mid2 = l - mid
            l1 = float('-inf')
            l2 =  float('-inf')
            r1 = float('inf')
            r2 = float('inf')
            if mid < n1: r1 = nums1[mid]
            if mid2 < n2: r2 = nums2[mid2]
            if mid - 1 >= 0: l1 = nums1[mid - 1]
            if mid2 - 1 >= 0: l2 = nums2[mid2 - 1]
            if l1 <= r2 and l2 <= r1:
                if n % 2 == 1: 
                    return max(l1, l2)
                return (max(l1,l2)+ min(r1,r2)) / 2
            elif l1 > r2:
                high = mid - 1
            else:
                low = mid + 1