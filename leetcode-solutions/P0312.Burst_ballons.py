# wrong submission
class Solution:
    def maxCoins(self, arr: List[int]) -> int:
        import copy 

        visited = [0] * len(arr)
        res = []
        def permute(r):
            if len(r) == len(arr):
                res.append(copy.deepcopy(r))
                return res
                
            for i in range(len(arr)):
                if not visited[i]:
                    visited[i]= 1
                    r.append(i)
                    permute(r)
                    visited[i] = 0
                    r.pop()
                
            return res
    
        orders = permute([])
        mx = float('-inf')

        for k, order in enumerate(orders):
            m = 0
            tmp = arr
            bursted = [0] * len(arr)
            for i in range(len(order)):
                idx = order[i]
                if idx == 0 :
                    m += ((tmp[idx]) * (tmp[idx+1] if bursted[idx+1] != 1 else 1))
                elif idx == len(arr)-1:
                    m += ((tmp[idx-1] if bursted[idx-1] != 1 else 1) * (tmp[idx]))
                else:
                    before = tmp[idx-1] if bursted[idx-1] != 1 else 1
                    at = tmp[idx] if bursted[idx] != 1 else 1
                    nxt = tmp[idx+1] if bursted[idx+1] != 1 else 1
                    m +=  (before * at  * nxt)
                mx = max(mx, m)
                bursted[idx] = 1
                
        return mx