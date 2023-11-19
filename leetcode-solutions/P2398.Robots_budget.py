class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        i = 0
        j = 0
        tc = 0
        rc = 0
        res = float('-inf')
        stck = []

        while i <= j and j < len(chargeTimes):
            while stck and stck[-1] < chargeTimes[j]:
                stck.pop()
            stck.append(chargeTimes[j])

            rc += runningCosts[j] 
            tc = stck[0] + (j-i+1) *  rc
            while tc > budget:
                if stck and stck[0] == chargeTimes[i]:
                    stck.pop(0)
                rc -= runningCosts[i] 
                i += 1
                tc = stck[0] + (j-i+1) *  rc if stck else 0
            
            res = max(res, j- i+1)

            j += 1

        return res