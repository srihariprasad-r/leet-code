# TLE
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        def getnextday(days, day, cday):
            if day >= len(days): return -1
            eday = days[day] + cday - 1

            while day < len(days) and days[day] <= eday:
                day += 1

            return day

        def recursion(idx):
            if idx >= len(days): return 0
            
            consective_days = 0
            total = float('inf')
            a = float('inf')
            b = float('inf')
            c = float('inf')
            for i in range(len(costs)):
                if i == 0: 
                    consective_days = 1
                    v = getnextday(days, idx, consective_days)
                    if v != -1:
                        a = costs[i] + recursion(v)  
                elif i == 1: 
                    consective_days = 7
                    v = getnextday(days, idx, consective_days)
                    if v != -1:                                        
                        b = costs[i] + recursion(v)  
                else:
                    consective_days = 30
                    v = getnextday(days, idx, consective_days)
                    if v != -1:
                        c = costs[i] + recursion(v) 

            total = min(total, min(a, min(b, c)))

            return total

        res = float('inf')
        res = min(res, recursion(0))

        return res


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        def recursion(idx, nxt, cost=float('inf')):
            if ((idx >= len(days)) or (nxt > days[-1])) : return cost

            take = float('inf')

            take = min(take, min(recursion(idx+1, days[idx] + 1, cost+ costs[0]),
                    recursion(idx+1, days[idx] + 7, cost+ costs[1]),
                    recursion(idx+1, days[idx] + 30, cost+ costs[2])))

            return take
        
        return recursion(0, 0, 0)                