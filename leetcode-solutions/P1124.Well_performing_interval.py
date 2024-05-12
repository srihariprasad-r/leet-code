# wrong submission
class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        td = [x//8  for x in hours]
        res = 0

        ntd_cnt = 0
        td_cnt = 0

        i = 0
        j = 0
        while i < len(td):
            if td[i] == 1:
                td_cnt += 1
            elif td[i] == 0:
                ntd_cnt += 1

            if td_cnt > ntd_cnt:
                res  = max(res, i -j + 1)
            else:
                while j <= i: 
                    j += 1
                    td_cnt = 0
                    ntd_cnt = 0
            i += 1

        return res