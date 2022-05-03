class Solution(object):
    def countUnguarded(self, m, n, guards, walls):
        """
        :type m: int
        :type n: int
        :type guards: List[List[int]]
        :type walls: List[List[int]]
        :rtype: int
        """
        dp = [[0] * n for _ in range(m)]

        for x, y in guards:
            dp[x][y] = 1

        for x, y in walls:
            dp[x][y] = 1

        directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]

        for x, y in guards:
            for dx, dy in directions:
                cur_x = x
                cur_y = y

                while 0 <= cur_x+dx < m and 0 <= cur_y+dy < n and dp[cur_x+dx][cur_y+dy] != 1:
                    cur_x += dx
                    cur_y += dy
                    dp[cur_x][cur_y] = 9

        return sum(1 for x in range(m) for y in range(n) if not dp[x][y])