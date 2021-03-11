class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stck = []
        ops = []
        import re
    
        j = 0
    
        s = re.sub(r' ','', s)

        while j < len(s):
            if s[j] != '(' and s[j] != '-' and s[j] != '+' and s[j] != ')':
                stck.append(int(s[j]))
            elif s[j] == '(':
                ops.append(s[j])
            elif s[j] == '+' or s[j] == '-':
                ops.append(s[j])
            elif s[j] != ' ':
                while len(ops)> 0 and ops[-1] != '(' and len(stck) > 0:
                    val2 = stck.pop()
                    val1 = stck.pop()
                    opv = ops.pop()
                    if opv == '+':
                        val = val1 + val2
                    else:
                        val = val1 - val2
                    stck.append(val)
                ops.pop()


            j += 1

        while len(ops) > 0 and len(stck) > 0:
            val1 = stck.pop()
            val2 = stck.pop()
            opv = ops.pop()
            if opv == '+':
                val = val1 + val2
            else:
                val = val1 - val2
            stck.append(val)  
         
        
        return stck[-1]