class Solution(object):
    def luckyNumbers (self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        min_row = set()
        max_col = set()
        for i in range(len(matrix)):
            row = min(matrix[i])
            min_row.add(row)
        
        for j in range(len(matrix[0])):
            i = 0
            max_val = 0
            while i < len(matrix):
                max_val = max(max_val, matrix[i][j])
                i += 1
            max_col.add(max_val)
        
        return min_row.intersection(max_col)