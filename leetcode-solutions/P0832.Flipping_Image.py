class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        temp = []
        ans = []
        res = []
        for i in range(len(image)):
            temp.insert(i, image[i][::-1])

        for i in range(len(temp)):
            tmp = temp[i]
            ans = []
            for j in range(len(tmp)):
                ans.insert(j,tmp[j] ^ 1)
            res.insert(i, ans)
                
        return res