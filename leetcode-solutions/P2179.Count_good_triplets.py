class Solution(object):
    def goodTriplets(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        from sortedcontainers import SortedList

        indices = [0] * len(nums1)
        map = {}
        cnt = 0

        for i, el in enumerate(nums1):
            map[el] = i

        for i, el in enumerate(nums2):
            indices[i] = map[el]

        lc = SortedList()
        rc = SortedList()
        left = []
        right = []
        for i, el in enumerate(indices):
            left.append(bisect_left(lc, el))
            lc.add(el)

        for i in range(len(indices)-1, -1, -1):
            right.append(len(rc) - bisect_right(rc, indices[i]))
            rc.add(indices[i])

        for i in range(len(indices)):
            cnt += left[i] * right[len(indices)-i-1]

        return cnt
