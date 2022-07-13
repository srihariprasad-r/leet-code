# TLE submission

class Solution(object):
    def scoreOfStudents(self, s, answers):
        """
        :type s: str
        :type answers: List[int]
        :rtype: int
        """
        points = 0
        
        def ans(i, j):
            if i == j:
                return [int(s[i])]
            
            ansSet = set()
            
            for sign in range(i+1, j, 2):
                for a in ans(i, sign-1):
                    for b in ans(sign+1, j):
                        output = a * b if s[sign] == '*' else a + b
                        if output <= 1000:
                            ansSet.add(output)
            
            return ansSet
        
        res = ans(0, len(s) - 1)
        actualValue = eval(s)
        
        for ans in answers:
            if ans == actualValue:
                points += 5
            elif ans in res:
                points += 2
                
        return points