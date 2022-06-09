class Solution(object):
    def minimizeResult(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        st = end = 0
        plus = -1
        preval = float('inf')

        for i in range(len(expression)):
            if expression[i] == '+':
                plus = i
                break

        for i in range(plus):
            for j in range(plus+1, len(expression)):
                n1 = 1
                n1Str = expression[0:i]
                if len(n1Str) > 0:
                    n1 = int(n1Str)

                n2Str = expression[i:plus]
                n2 = int(n2Str)

                n3Str = expression[plus+1:j+1]
                n3 = int(n3Str)

                n4 = 1
                n4Str = expression[j+1:]
                if len(n4Str) > 0:
                    n4 = int(n4Str)

                cal = n1 * (n2+n3) * n4
                if cal < preval:
                    preval = cal
                    st = i
                    end = j+1

        ans = ''
        ans += expression[0:st]
        ans += '('
        ans += expression[st:end]
        ans += ')'
        ans += expression[end:]

        return ans