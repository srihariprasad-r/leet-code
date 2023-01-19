class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        def subseq(s1, s2, arr):
            s = 0
            t = 0
            cnt = 0

            while s < len(s1) and t < len(s2):
                if s in arr:
                    s += 1
                    continue
                if s1[s] == s2[t]:
                    t += 1
                    cnt += 1
                s += 1

            return cnt == len(s2)

        l = 0
        r = len(removable) - 1
        ans = 0

        while l <= r:
            mid = l + (r-l)//2

            if subseq(s, p, set(removable[:mid+1])):
                ans = max(ans, mid+1)
                l = mid + 1
            else:
                r = mid - 1

        return ans