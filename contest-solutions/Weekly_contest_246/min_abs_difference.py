# TLE

class Solution(object):
    def minDifference(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        diff = []
        mindiff = float('inf')
        
        if len(set(nums)) == 1:
            diff = [-1] * len(queries)
            return diff
    
        for i in range(len(queries)):
            idx = queries[i]
            sublist = nums[idx[0]:idx[1]+1]
            if len(sublist) == 1:
                diff.append(sublist[-1])
            elif len(sublist) == 2:
                if abs(sublist[0] - sublist[1]) == 0:
                    diff.append(-1)
                else:
                    diff.append(abs(sublist[0] - sublist[1]))
            else:
                mindiff = float('inf')
                for m in range(len(sublist)):
                    n = m + 1
                    while n < len(sublist):
                        if (sublist[m] == sublist[n]):
                            n += 1
                            continue
                        elif abs(sublist[m] - sublist[n]) < mindiff:
                            if mindiff == 0:
                                continue
                            else:
                                mindiff = abs(sublist[m] - sublist[n])
                        n += 1
                if mindiff == 0: 
                    diff.append(-1)
                else:
                    diff.append(mindiff)

        return diff