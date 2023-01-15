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
            # check if there is asteriod < 0 (moving left) and one > 0 (moving right)
            while len(stck) > 1 and stck[-1] < 0 and stck[-2] > 0:
                el = stck.pop()
                if stck[-1] > abs(el):
                    continue
                else:
                    if abs(el) == stck[-1]: 
                        stck.pop()
                    else:
                        stck.pop()
                        stck.append(el)

        return stck