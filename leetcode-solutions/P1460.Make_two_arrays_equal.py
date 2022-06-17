class Solution(object):
    def canBeEqual(self, target, arr):
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: bool
        """
        val = {}
        for i in range(len(arr)):
            if not(arr[i] in val):
                val[arr[i]] = 1
            else:
                val[arr[i]] += 1
            
        for i in range(len(target)):
            if target[i] in val:
                val[target[i]] -= 1
                if val[target[i]] == 0:
                    del val[target[i]]
            
        return True if len(val) == 0 else False