#wrong submission

class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        
        f = lambda x, y: max(x) if y == 'max' else min(x)
        max_arr1 , min_arr1 = f(arr1, 'max') , f(arr1, 'min')
        max_arr2, min_arr2 = f(arr2, 'max') , f(arr2, 'min')
        
        num_el = max(abs(max_arr1 - min_arr2), abs(max_arr2 - min_arr1))
        
        res = [0] * (num_el + 1)
        
        for i in range(len(arr1)):
            for j in range(len(arr2)):
                diff = abs(arr1[i] - arr2[j])
                res[diff] += 1

        return len(list(x for x in res if x == d))