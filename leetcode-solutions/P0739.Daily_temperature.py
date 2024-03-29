class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        res = [0] * len(T)
        stck = []
        for i, val in enumerate(T):
            while len(stck) > 0 and T[i] > T[stck[-1]]:
                idx = stck.pop()
                res[idx] = i - idx
            stck.append(i)
        
    
        return res

# Method 2 - wrong submission

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stck = [0]* len(temperatures)
        
        for i in range(len(temperatures)-1):
            j = i + 1
            if temperatures[i] == temperatures[j]:
                continue
            while j < len(temperatures):
                if temperatures[i] < temperatures[j]:
                    stck[i] = j-i
                    break
                j += 1

                
        return stck

# Method 3

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = []
        ans = [0] * len(temperatures)
        for i in range(len(temperatures)-1, -1, -1):
            while s and s[-1][1] <= temperatures[i]:
                s.pop()
            ans[i] = 0 if not s else s[-1][0] - i
            s.append((i, temperatures[i]))

        return ans