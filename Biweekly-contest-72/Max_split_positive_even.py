# Incorrect submission

class Solution(object):
    def maximumEvenSplit(self, finalSum):
        """
        :type finalSum: int
        :rtype: List[int]
        """
        import copy

        if finalSum % 2 == 1:
            return []

        even_nums = [x for x in range(2, finalSum) if x % 2 == 0]

        mp = {}

        for i in range(len(even_nums)):
            if not(even_nums[i] in mp):
                mp[even_nums[i]] = 1
            else:
                mp[even_nums[i]] += 1

        def solution(idx, lst, tgt, mp, ans=[], res=[]):
            if tgt < 0:
                return

            if tgt == 0:
                if len(res) > 0:
                    if len(res[-1]) < len(ans):
                        res = []
                        return res.append(ans)
                else:
                    return res.append(ans)

            # if idx == len(lst):
            #     return res.append(copy.deepcopy(ans))

            for i in range(idx, len(lst)):
                solution(i+1, lst, tgt-lst[i], mp, ans + [lst[i]], res)

            return res

        return solution(0, even_nums, finalSum, mp)
