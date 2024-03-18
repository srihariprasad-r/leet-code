# wrong submission

class Solution:
    def maxOperations(self, arr: List[int], k: int) -> int:
        import collections
        from collections import deque
        d = collections.defaultdict(list)
        for i in range(len(arr)-1):
            j = i + 1
            s = arr[i]
            while j < len(arr):
                s += arr[j]
                if s == k:
                    d[s].append((i,j))
                    
                if s in d: 
                    if (i,j) not in d[s]:
                        d[s].append((i,j))
                else:
                    d[s].append((i,j))
                
                    
                s -= arr[j]
                j += 1
                
        q = deque()
        
        m, n = d[k][0]
        
        for i in range(1, len(d[k])):
            q.append(d[k][i])
        
        cnt = 1
        
        while q:
            x, y = q.popleft()
            if x == m or y == n or x == n or y == m:
                continue
            else:
                cnt += 1
                
        return cnt