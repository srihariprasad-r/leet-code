# wrong submission

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        q = deque()
        visited = set()
        visited.add((0,0))
        steps = 0
        dirs = [(-1,0), (1, 0), (0, 1), (0, -1)]
        q.append((0, 0))

        while q:
            t = len(q)
            for _ in range(t):
                c = q.popleft()
                if c[0] >= m or c[1] >= n: 
                    return steps
                for d in dirs:
                    new_x, new_y = c[0] + d[0], c[1] + d[1]
                    if 0 <= new_x < m and 0 <= new_y < n and (new_x, new_y) not in visited:
                        if matrix[c[0]][c[1]] < matrix[new_x][new_y]: 
                            continue
                        c = tuple([new_x, new_y])
                        q.append(c)
                        visited.add((new_x, new_y))
            steps += 1

        return steps