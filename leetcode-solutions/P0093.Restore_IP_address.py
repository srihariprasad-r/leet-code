class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        import copy

        def valid(s):
            if len(s) > 3 or len(s) < 1:
                return False
            elif s[0] == '0' and len(s) > 1:
                return False
            elif int(s) > 255:
                return False

            return True

        def helper(s, idx, dots, arr=[], res=[]):
            if dots == 3:
                if valid(s[idx:]):
                    arr.append('.' + s[idx:])
                    res.append(''.join(copy.deepcopy(arr)))
                    return

            for i in range(idx, len(s)):
                if valid(s[idx:i+1]):
                    if dots == 0:
                        tmp = s[idx:i+1]
                    else:
                        tmp = str('.' + s[idx:i+1])

                    # arr.append(tmp)
                    helper(s, i+1, dots + 1, arr + [tmp], res)
                    # del arr[-1]

            return res

        return helper(s, 0, 0)