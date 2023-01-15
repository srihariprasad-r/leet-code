class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stck = []
        for i in range(len(asteroids)):
            stck.append(asteroids[i])
            while len(stck) > 1 and stck[-1] < 0 and stck[-2] > 0:
                pval = stck.pop()
                if abs(pval) > stck[-1]:
                    stck.pop()
                    stck.append(pval)
                elif abs(pval) < stck[-1]:
                    continue
                else:
                    stck.pop()
          
        return stck

# Method 2 - slight variation(wrong submission):

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stck = []

        for i in range(len(asteroids)):
            stck.append(asteroids[i])
            while len(stck) > 1 and ((stck[-2] > 0 and stck[-1] < 0) \
                    or (stck[-1] > 0 and stck[-2] < 0)):
                el = stck.pop()
                if abs(stck[-1]) > abs(el):
                    continue
                else:
                    if abs(el) == abs(stck[-1]): 
                        stck.pop()
                    else:
                        stck.pop()
                        stck.append(el)

        return stck