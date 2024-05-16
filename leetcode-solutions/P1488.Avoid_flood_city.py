# wrong submission
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        res = [-1]* len(rains)
        stck = []

        for i in range(len(rains)):
            if rains[i] > 0 : 
                stck.append(rains[i])
                continue
            if stck: res[i] = stck.pop()

        return res