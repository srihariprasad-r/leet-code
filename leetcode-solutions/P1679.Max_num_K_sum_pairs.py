# wrong submission

class Solution:
    def maxOperations(self, arr: List[int], k: int) -> int:
        import collections
        d = collections.defaultdict(int)
        used = collections.defaultdict(int)
        visited = [0] * (max(arr)+1)
        cnt = 0

        for i in range(len(arr)):
            s = k - arr[i]
            if s in d:
                d[s] += 1
            else:
                d[s] = 1

        for i in range(len(arr)):
            if arr[i] not in used:
                if k-arr[i] not in used:
                    if arr[i] == k-arr[i]:
                        if d[arr[i]] > 1: cnt += 1
                    else:
                        cnt += min(d[arr[i]], d[k-arr[i]])
                    used[arr[i]] = i
                    used[k-arr[i]] = i
                
        return cnt