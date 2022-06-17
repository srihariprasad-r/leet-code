class Solution(object):
    def busyStudent(self, startTime, endTime, queryTime):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type queryTime: int
        :rtype: int
        """
        diff_array = [-1] * len(startTime)
        cnt = 0 
        
        one_array = zip(startTime, endTime)
        for i in range(len(one_array)):
            if one_array[i][0] <= queryTime and  one_array[i][1] >= queryTime:
                diff_array[i] = one_array[i][1] - one_array[i][0]
                
                if diff_array[i] >= 0:
                    cnt += 1
        
        return cnt