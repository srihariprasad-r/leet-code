class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        def recursion(idx, ct, pt):
            if ct > n: return 0

            if idx == len(profit): 
                if pt >= minProfit: return 1
                return 0

            take = 0
            no_take = 0
            take = recursion(idx+1, ct + group[idx], min(pt + profit[idx], minProfit))
            no_take = recursion(idx+1, ct, pt)

            return take + no_take

        return recursion(0, 0, 0)        