# Wrong submission

class Solution(object):
    def numsSameConsecDiff(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        def backtrack(idx, n, k, lst, res=[]):
            if len(lst) == n:
                is_not_right_number = False
                cur = 0
                while not is_not_right_number:
                    if cur < len(lst) -1:
                        if abs(lst[cur]- lst[cur+1]) == k:
                            continue
                        else:
                            is_not_right_number = True
                            break
                    cur += 1
                if not is_not_right_number:
                    el = int(''.join([str(i) for i in lst]))
                    if el not in res:
                        res.append(el)
                        lst = []
                    return
            
            for i in range(1, 10):
                lst.append(i+1)
                backtrack(i+1, n, k, lst, res)
                lst.pop()
                
            return res
        
        curList = []

        return backtrack(1, n, k, curList)