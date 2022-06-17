# some errors exists, need revisit

class Solution(object):
    def mergeTriplets(self, triplets, target):
        """
        :type triplets: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        if len(triplets) == 1 and target == triplets[-1]: return True
        i = 0
        j = i + 1
        while i < j and j < len(triplets):
            temp = []
            a, b = triplets[i], triplets[j]
            temp = list(max(c) for c in zip(a,b))
            cnt = 0
            flag = [False] * len(target)
            eq = [False] * len(target)
            for c in temp:
                if target[cnt] >= c: 
                    flag[cnt] = True
                    if target[cnt] == c:
                        eq[cnt] = True
                cnt += 1
            if eq.count(True) == len(eq):
                return True
            if flag.count(True) == len(flag):
                triplets[j] = temp
                i = j
                j += 1
            else:
                j += 1

        return False