class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l1 = len(nums1)
        l2 = len(nums2)

        left = 0
        right = l1 if l1 < l2 else l2
        right = right * 2

        max_left_y, max_left_x, min_right_x, min_right_y = -1, -1, -1, -1

        while left <= right:
            mid = left + (right - left) / 2
            pt_y = l1+l2 - mid

            if mid == 0:
                max_left_x = -float('inf')
            else:
                max_left_x = nums1[(mid-1)/2]

            if mid == l1*2:
                min_right_x = float('inf')
            else:
                min_right_x = nums1[mid/2]

            if pt_y == 0:
                max_left_y = -float('inf')
            else:
                max_left_y = nums2[(pt_y - 1)/2]

            if pt_y == l2*2:
                min_right_y = float('inf')
            else:
                min_right_y = nums2[pt_y/2]

            if max_left_x <= min_right_y and max_left_y <= min_right_x:
                if (l1 + l2) % 2 == 0:
                    return float(max(max_left_x, max_left_y)
                                 + min(min_right_x, min_right_y)) / 2
            elif max_left_x > min_right_y:
                right = mid - 1
            else:
                left = mid + 1

        return -1
