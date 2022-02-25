class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        map = {}
        for i in range(len(s)):
            map[s[i]] = i

        arr = [x for x in s]
        left = right = index = 0
        res = []
        
        while index < len(arr):
            ch = arr[index]
            curr = map[ch]
            
            right = max(right, curr)
            if right == index:
                size = right - left + 1
                res.append(size)
                right += 1
                left = right
            
            index += 1
        
        return res