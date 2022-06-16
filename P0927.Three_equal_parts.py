class Solution(object):
    def threeEqualParts(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        if arr.count(1) == 0:
            return [0, 2]
        
        if arr.count(1) % 3:
            return [-1, -1]
        
        tgt = arr.count(1) // 3
        p1 = p2 = p3 = 0
        cnt = 0
        for i, el in enumerate(arr):
            if el == 1:
                if cnt == 0:
                    p1 = i
                elif cnt == tgt:
                    p2 = i
                elif cnt == 2*tgt:
                    p3 = i
                    
                cnt += 1
            
        n = len(arr)

        p2_old = p2
        p3_old = p3
        
        while p3 < n and p1 < p2_old and p2 < p3_old:
            if arr[p1] != arr[p2] or arr[p1] != arr[p3]:
                return [-1, -1]
            else:
                p1 += 1
                p2 += 1
                p3 += 1

        return [p1-1, p2] if p3 == n else [-1, -1]
            