class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        dct = {}

        if len(trust) == 0:
            if n == 1:
                return 1
            else:
                return -1

        for i in range(len(trust)):
            dep, nondep = trust[i][0], trust[i][1]
            dct.setdefault(nondep, []).append(dep)

        judge = list(k for k, v in dct.items() if len(v) == n - 1)

        is_he_judge = {True for v in dct.values() for i in range(
            len(v)) if v[i] == judge[0]} if judge else False

        return judge[0] if judge and not(is_he_judge) else -1
