class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        lst = []
        for ps, st, end in trips:
            lst.append((st, ps))
            lst.append((end, -ps))

        lst.sort()

        for _, ps in lst:
            capacity -= ps
            if capacity < 0:
                return False

        return True
