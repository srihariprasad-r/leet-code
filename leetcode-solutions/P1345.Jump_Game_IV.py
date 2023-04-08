# TLE

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        q = [(arr[0], 0, 0)]
        visited = [0]
        # steps = 0
        res = float('inf')

        while q:
            for _ in range(len(q)):
                el, pos, s = q.pop(0)
                if pos == len(arr) - 1:
                    res = min(res, s)
                for i in range(pos+1, len(arr)):
                    if i not in visited and el == arr[i]:
                        q.append((arr[i], i, s + 1))
                        visited.append(i)
                    if pos > 0 and pos < len(arr):
                        if (pos-1) not in visited:
                            q.append((arr[pos-1], pos-1, s + 1))
                            visited.append(pos-1)
                    if pos < len(arr):
                        if (pos+1) not in visited:
                            q.append((arr[pos+1], pos+1, s + 1))
                            visited.append(pos+1)
            
        return -1 if res == float('inf') else res