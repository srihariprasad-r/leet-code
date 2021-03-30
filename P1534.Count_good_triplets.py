class Solution(object):
    def countGoodTriplets(self, arr, a, b, c):
        """
        :type arr: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        cnt = 0

        for i in range(len(arr)-2):
            for j in range(i+1,len(arr)-1):
                p1, p2 = i, j 
                if abs(arr[p1] - arr[p2]) <= a:
                    for m in range(j+1, len(arr)):
                        p3 = m
                        if abs(arr[p2] - arr[p3]) <= b and  abs(arr[p1] - arr[p3]) <= c:
                            cnt += 1
        return cnt