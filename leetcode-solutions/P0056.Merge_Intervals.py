# wrong submission

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []

        for intr in intervals:
            x, y = intr[0], intr[1]
            if not ans:
                ans.append((x, y))
            else:
                newx, newy = ans[-1]
                if newx <= x <= newy and y >= newy:
                    ans.pop()
                    ans.append((newx, y))
                else:
                    ans.append((x, y))

        return ans
