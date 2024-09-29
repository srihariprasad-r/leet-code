class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        def recursion(idx, ct):
            if idx >= len(profit): return 0

            take = 0
            no_take = 0
            if ((ct + group[idx] <= n) and (profit[idx] >= minProfit)):
                take = 1 + recursion(idx, ct + group[idx])
            else:
                no_take = recursion(idx+1, 0)

            return take + no_take

        return recursion(0, 0)        