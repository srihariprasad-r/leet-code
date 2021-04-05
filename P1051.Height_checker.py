class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        cnt = 0
        copyArr = copy.deepcopy(heights)
        
        heights.sort()
        for i in range(len(copyArr)):
            if copyArr[i] != heights[i]:
                cnt += 1
        
        return cnt