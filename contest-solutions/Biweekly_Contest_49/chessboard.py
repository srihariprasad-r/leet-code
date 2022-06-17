class Solution(object):
    def squareIsWhite(self, coordinates):
        """
        :type coordinates: str
        :rtype: bool
        """
        chessboard = [
            [0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0]        
        ]
        
        row, col = coordinates[0], coordinates[1]
        
        if row == 'a' or row == 'c' or row == 'e' or row == 'g':
            return True if chessboard[0][int(col)-1] else False
        else:
            return True if chessboard[1][int(col)-1] else False