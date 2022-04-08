class Solution(object):
    def numsSameConsecDiff(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        def backtrack(idx, n, k, lst, res=[]):
            if len(lst) == n:
                if lst[0] != 0:
                    intEl = int(''.join([str(i) for i in lst]))
                    if intEl not in res:
                        res.append(intEl)
                return res
            
            el = lst[-1] 
            
            if el + k <= 9:
                lst.append(el + k)
                backtrack(idx, n, k, lst, res)
                lst.pop()

            if el - k >= 0:
                lst.append(el - k)
                backtrack(idx, n, k, lst, res)
                lst.pop()

            return res
        
        for i in range(10):
            res = backtrack(i, n, k, [i])

        return res