class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        q = deque()
        visited = [[0 for _ in range(len(image[0]))] for _ in range(len(image))]

        q.append((sr, sc, image[sr][sc]))
        visited[sr][sc] = 1

        direction = [(0, 1), (0,-1), (-1, 0), (1,0)]

        while q:
            i, j, c = q.popleft()
            image[i][j] = color
            visited[i][j] = 1

            for d in direction:
                x = i + d[0]
                y = j + d[1]
                if x > -1 and x < len(image) and y > -1 and y < len(image[0])\
                    and visited[x][y] == 0 and image[x][y] == c:
                    q.append((x, y, image[x][y]))

        return image