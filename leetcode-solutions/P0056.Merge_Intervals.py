class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        intervals = sorted(intervals, key=lambda x: x[0])

        for intr in intervals:
            x, y = intr[0], intr[1]
            if not ans:
                ans.append((x, y))
            else:
                newx, newy = ans[-1]
                if newy >= x:
                    ans.pop()
                    ans.append((newx, max(newy, y)))
                else:
                    ans.append((x, y))

        return ans

# Method 2
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])

        s = [intervals[0]]
        
        for i in range(1,len(intervals)):
            e, v = s[-1]
            if v >= intervals[i][0]:
                s.pop(-1)
                s.append((e, intervals[i][1] if v < intervals[i][1] else v))
            else:
                s.append(intervals[i])

        return s  