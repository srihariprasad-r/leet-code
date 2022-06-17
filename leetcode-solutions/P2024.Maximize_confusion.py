class Solution(object):
    def maxConsecutiveAnswers(self, answerKey, k):
        """
        :type answerKey: str
        :type k: int
        :rtype: int
        """
        i, j = 0, 0
        mlen = 0
        t_cnt, f_cnt = 0, 0

#         if len(answerKey) == 1 and k <= 1:
#             return 1

        while j < len(answerKey):
            if answerKey[j] == 'T':
                t_cnt += 1
            elif answerKey[j] == 'F':
                f_cnt += 1

            mcnt = min(t_cnt, f_cnt)

            if mcnt <= k:
                mlen = max(mlen, j - i + 1)
            elif mcnt > k:
                while mcnt > k:
                    if answerKey[i] == 'T':
                        t_cnt -= 1
                    else:
                        f_cnt -= 1
                    mcnt = min(t_cnt, f_cnt)
                    i += 1

            j += 1

        return mlen
