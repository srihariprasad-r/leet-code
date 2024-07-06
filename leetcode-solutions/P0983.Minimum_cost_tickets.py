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