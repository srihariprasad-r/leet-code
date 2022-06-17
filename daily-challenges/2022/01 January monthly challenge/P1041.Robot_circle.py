class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        dirX, dirY = 0, 1  # initial position
        x, y = 0, 0

        for m in instructions:
            if m == 'G':
                x, y = x + dirX, y + dirY
            elif m == 'L':
                dirX, dirY = -1 * dirY, dirX
            else:
                dirX, dirY = dirY, -1 * dirX

        return (x, y) == (0, 0) or (dirX, dirY) != (0, 1)
