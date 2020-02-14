class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        str_var = int(''.join(str(d) for d in digits)) + 1
        int_list = [int(x) for x in str(str_var)]
        return int_list