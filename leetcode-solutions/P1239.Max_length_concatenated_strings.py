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
        
# wrong submission
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        if len(arr) == 1: return len(set(arr[-1]))
        mx = float('-inf')
        for i in range(len(arr)-1):
            for j in range(i+1, len(arr)):
                len1 = len(set(arr[i]))
                len2 = len(set(arr[j]))
                if len1 + len2 > mx:
                    mx = len1 + len2

        return mx        