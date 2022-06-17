class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        cnt_arr2 = {}
        only_in_arr1 = []
        ans = []
        for n in arr2:
            cnt_arr2[n] = 0
            
        for k in arr1:
            if k in cnt_arr2:
                cnt_arr2[k] += 1
            else:
                only_in_arr1.append(k)
                
        for m in arr2:
            ans.extend([m]* cnt_arr2[m])

        if len(only_in_arr1) > 0:
            only_in_arr1.sort()
            for i in range(len(only_in_arr1)):
                ans.append(only_in_arr1[i])
                
        return ans