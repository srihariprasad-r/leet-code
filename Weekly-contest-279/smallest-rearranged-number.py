# TLE failure

class Solution(object):
    def smallestNumber(self, num):
        """
        :type num: int
        :rtype: int
        """
        import copy

        d = str(num)
        n = len(d)
        mp = {}
        is_negative = False if d.find('-') < 0 else True
        new_input = d[1:] if is_negative else d

        for i in range(len(new_input)):
            if not(new_input[i] in mp):
                mp[new_input[i]] = 1
            else:
                mp[new_input[i]] += 1

        def solution(idx, s, mp, ans='', res=[]):
            if idx == len(s):
                res.append(int(ans))
                return

            for k, v in mp.items():
                if v > 0:
                    mp[k] -= 1
                    solution(idx+1, s, mp, ans + k, res)
                    mp[k] += 1

            return res

        arr = solution(0, new_input, mp)
        return min(arr) if not is_negative else int('-' + str(max(arr)))
