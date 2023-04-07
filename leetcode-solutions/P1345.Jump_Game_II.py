# wrong submission

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        q = [(arr[0], 0)]
        visited = [(arr[0], 0)]
        steps = 0

        while q:
            el, pos = q.pop()
            if pos == len(arr) - 1:
                return steps
            for i in range(pos+1, len(arr)):
                if (arr[i], pos+i) not in visited and arr[pos] == arr[i]:
                    q.append((arr[i], pos+i))
                    visited.append((arr[i], pos+1))
            if pos > 0 and pos < len(arr):
                if (arr[pos], pos-1) not in visited:
                    q.append((arr[pos], pos-1))
                    visited.append((arr[pos], pos-1))
            if pos < len(arr):
                if (arr[pos], pos+1) not in visited:
                    q.append((arr[pos], pos+1))
                    visited.append((arr[pos], pos+1))
            steps += 1

        return -1