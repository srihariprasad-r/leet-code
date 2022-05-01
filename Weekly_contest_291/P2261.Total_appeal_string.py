# TLE submission

class Solution(object):
    def appealSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        cum_cnt = 0
        appeal_cnt = {}
        jump = 0

        for i in range(len(s)):
            appeal_str = ''
            jump += 1
            for j in range(i, len(s)):
                appeal_str += s[j:j+jump]
                appeal_cnt.setdefault(len(set(appeal_str)), []).append(appeal_str)

            jump = 0

        for k, v in appeal_cnt.items():
            cum_cnt += len(v)*k

        return cum_cnt