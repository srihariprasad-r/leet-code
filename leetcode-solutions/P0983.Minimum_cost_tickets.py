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
        dp = [float('inf')] * len(days)

        def getnextday(i, inc):
            st = days[i]
            end = inc

            while i < len(days) and days[i] <= st + end - 1:
                i += 1

            return i

        def recursion(idx, cost=float('inf')):
            if idx >= len(days) : return 0

            if dp[idx] != float('inf'): return dp[idx]

            take = float('inf')

            nxt_idx_1_day = getnextday(idx, 1)
            nxt_idx_7_day = getnextday(idx, 7)
            nxt_idx_30_day = getnextday(idx, 30)

            one_day = costs[0] + recursion(nxt_idx_1_day)
            seven_day = costs[1] + recursion(nxt_idx_7_day)
            thirty_day = costs[2] + recursion(nxt_idx_30_day)                        

            lowest = min(one_day, min(seven_day, thirty_day))

            dp[idx] = min(dp[idx], lowest)                    

            return dp[idx]
        
        return recursion(0)                        