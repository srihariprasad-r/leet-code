class Solution(object):
    def minimumRemoval(self, beans):
        """
        :type beans: List[int]
        :rtype: int
        """
        min_el = float('inf')
        sum_beans = sum(beans)
        beans.sort()

        for i in range(len(beans)):
            min_el = min(min_el, sum_beans-(beans[i] * (len(beans) - i)))

        return min_el
