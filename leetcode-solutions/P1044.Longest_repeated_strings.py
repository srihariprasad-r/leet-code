class Solution(object):
    def longestDupSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        nums = [ord(c)-ord('a') for c in s]

        def f(idx):
            hash1 = set()
            base = 26
            # 2 **32 is failing - so added 2**64+1 to avoid collision
            mod = 2 ** 64 + 1
            # added for TLE
            e = pow(base, idx, mod)
            cur = 0
            for i in range(idx):
                cur = cur * base + nums[i]

                cur %= mod

            hash1.add(cur)

            for i in range(idx, n):
                cur = cur * base + nums[i] - nums[i-idx] * e
                cur %= mod
                if cur in hash1:
                    return i - idx + 1

                hash1.add(cur)

            return -1

        l = 0
        r = n - 1
        ans = 0

        while l < r:
            mid = l + (r-l+1)//2
            st = f(mid)
            if st >= 0:
                l = mid
                ans = st
            else:
                r = mid - 1

        return s[ans:ans+l]