class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        mx = float('-inf')
        
        less_left_el_stck = [0] * len(heights)
        great_right_el_stck = [len(heights)-1] * len(heights)
        
        for i in range(1, len(heights)):
            j = i - 1
            left_stck = []
            left_stck.append(i)
            in_flag = False
            while j >= 0:
                if heights[left_stck[-1]] > heights[j]:
                    left_stck.pop()
                    left_stck.append(j)
                    in_flag = True
                    break
                j -= 1
            if in_flag:
                less_left_el_stck[i]= j + 1
            
        for i in range(len(heights)-1, -1, -1):
            j = i + 1
            right_stck = []
            right_stck.append(i)
            in_flag = False
            while j < len(heights) :
                if heights[right_stck[-1]] > heights[j]:
                    right_stck.pop()
                    right_stck.append(j)
                    in_flag = True
                    break
                j += 1
            if in_flag:
                great_right_el_stck[i]= j - 1
            
        for i in range(len(less_left_el_stck)):
            mx = max(mx, (great_right_el_stck[i] - less_left_el_stck[i] +  1) * heights[i])
            
        return mx
                