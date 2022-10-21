class Solution(object):
    def findLength(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        """
        [1, 2, 3]
        cur = 0
        1   -> cur = cur*base + num = 1
        12  -> cur = cur*base + num = 12
        123 -> cur = cur*base + num = 123
        
        23 = 123 - 100 = cur - base ** (2 - 0)
        """

        def f(idx):
            hash1 = set()
            hash2 = set()
            base = 101
            mod = 2**32

            cur = 0
            for i in range(m):
                cur = cur * base + nums1[i]

                if i >= idx:
                    cur -= nums1[i-idx] * base ** idx

                cur %= mod
                if i >= mid - 1:
                    hash1.add(cur)

            cur = 0
            for i in range(n):
                cur = cur * base + nums2[i]

                if i >= idx:
                    cur -= nums2[i-idx] * base ** idx

                cur %= mod
                if i >= mid - 1:
                    hash2.add(cur)

            return len(hash1.intersection(hash2)) > 0

        m = len(nums1)
        n = len(nums2)

        l = 0
        r = min(m, n)

        while l < r:
            mid = l + (r - l+1)//2

            if f(mid):
                l = mid
            else:
                r = mid - 1

        return l
