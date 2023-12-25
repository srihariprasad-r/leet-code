class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []

        def dfs(idx, arr=[]):
            if len(arr) == k:
                res.append(copy.deepcopy(arr))
                return

            for i in range(idx, n+1):
                dfs(i+1, arr + [i])

            return res

        return dfs(1)

# Method 2 - similar to above

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(idx, arr, res):
            if len(arr) == k:
                if arr not in res:
                    res.append(copy.deepcopy(arr))

                return

            for i in range(idx, n+1):
                if i not in arr:
                    arr.append(i)
                    dfs(i+1, arr, res)
                    arr.pop()

            return res
        
        return dfs(1, [], [])

# method 3
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def recurse(idx, k, a):
            if k == len(a):
                ans.append(a[:])
                return
            # ans.append(a[:])
    
            for i in range(idx, n+1):
                a.append(i)
                recurse(i + 1,k, a)
                a.pop()
        
            return ans

        return recurse(1,k,[])