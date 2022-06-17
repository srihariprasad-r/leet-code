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
        
        