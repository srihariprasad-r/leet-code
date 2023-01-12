# wrong submission

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        gap = defaultdict(int)

        width = sum(wall[0])
        for i in range(len(wall)):
            l = wall[i][0]
            for j in range(1, len(wall[i])):
                gap[l] += 1
                l += wall[i][j]

        max_gap = max(gap.values() or [0])

        return len(wall) - max_gap
