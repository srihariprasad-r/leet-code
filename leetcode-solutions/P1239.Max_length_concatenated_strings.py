# Wrong Submission

class Solution(object):
    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        """
        def func(lst):
            return map(str, lst)
        
        def backtrack(idx, arr, curList, ans=0):
            if idx == len(arr):
                return ans
            
            if curList:
                el = ''.join(func(curList))
                if len(el) == len(set(el)):
                    ans = max(ans, len(el))
                return ans

            for i in range(idx+1, len(arr)):
                curList.append(arr[i])
                ans = max(ans, backtrack(i, arr, curList, ans))
                curList.pop()
            
            return ans
        
        curList = []
        ans = 0
        
        for i in range(0, len(arr)):
            curList.append(arr[i])
            ans = max(ans, backtrack(i, arr, curList, ans))
            curList.pop()
            
        return ans
        
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def dups(s1):
            d = [0] * 26
            for i in range(len(s1)):
                if d[ord(s1[i])-ord('a')]: return True
                d[ord(s1[i]) - ord('a')] = 1
            
            return False

        def recursion(idx, s):
            if idx >= len(arr): return len(s) if not dups(s) else 0

            include = 0
            if not dups(arr[idx]):
                include = recursion(idx+1, s + arr[idx])
            exclude = recursion(idx+1, s)

            return max(include, exclude)
        
        return recursion(0, '')        