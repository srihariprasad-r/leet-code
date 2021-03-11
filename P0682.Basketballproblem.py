class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        stck = []

        j = 0
        while j < len(ops):
            if ops[j] != 'C' and ops[j] != 'D' and not(ops[j] == '+'):
                stck.append(int(ops[j]))
            elif ops[j] == 'C':
                cnt = 1
                while cnt > 0:
                    stck.pop()
                    cnt -= 1
            elif ops[j] == 'D':
                val = stck[-1] if len(stck) > 0 else 0
                stck.append(val * 2)
            else:
                val1 = stck[-1]
                val2 = stck[-2]
                stck.append(val1+val2)
            
            j += 1
        
        return sum(stck)