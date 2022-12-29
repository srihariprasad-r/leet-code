# wrong submission

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        gap = {}

        for i in range(len(wall)):
            l = 0
            for j in range(len(wall[i])-1):
                l += wall[i][j]
                if l not in gap:
                    gap[l] = 1
                else:
                    gap[l] += 1

        mx = 0
        max_gap = 0
        for k, v in gap.items():
            if v > mx:
                mx = v
                max_gap = k

        return len(wall) - max_gap
