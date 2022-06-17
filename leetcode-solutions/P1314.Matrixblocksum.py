class Solution(object):
    def matrixBlockSum(self, arr, k):
        """
        :type mat: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        presum = [[0 for i in range(len(arr[0])+1)] for j in range(len(arr)+1)]

        for i in range(1,len(arr)+1):
            for j in range(1,len(arr[0])+1):
                presum[i][j] =  arr[i-1][j-1] + presum[i-1][j] + presum[i][j-1] \
                - presum[i-1][j-1]
            
        answer = [[0 for i in range(len(arr[0]))] for j in range(len(arr))]
    
        for i in range(1, len(arr)+1):
            for j in range(1, len(arr[0])+1):
                st_i, st_j = max(1, i -k) , max(1, j - k)
                end_i, end_j = min(len(arr), i+k) , min(len(arr[0]), j + k)
                answer[i-1][j-1] = presum[end_i][end_j] - presum[st_i-1][end_j] \
                    - presum[end_i][st_j-1] + presum[st_i-1][st_j-1]

        return answer