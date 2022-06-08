class Solution(object):
    def maxConsecutive(self, bottom, top, special):
        """
        :type bottom: int
        :type top: int
        :type special: List[int]
        :rtype: int
        """
        st = bottom
        end = top
        ans = 0

        for i in range(len(special)):
            diff = special[i] - st
            ans = max(ans, diff)
            st = special[i]+1

        ans = max(ans, end - special[-1])

        return ans
