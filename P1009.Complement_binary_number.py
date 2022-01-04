class Solution(object):
    def bitwiseComplement(self, n):
        """
        :type n: int
        :rtype: int
        """
        bin_val = bin(n)[2:]

        def f(x): return '0' if x == '1' else '1'

        tmp = ''
        for i in range(len(bin_val)):
            tmp += f(bin_val[i])

        return int("0b" + tmp, 2)