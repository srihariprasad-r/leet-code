class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s
        
        row = 0
        res = [[] for i in range(numRows)]

        shift = -1

        for i in s:
            res[row].append(i)
            if row == 0 or row == numRows - 1:
                shift *= -1
            row += shift

        for i in range(len(res)):
            res[i] = ''.join(res[i])
  
        return ''.join(res)