class Solution(object):
    def minimumCardPickup(self, cards):
        """
        :type cards: List[int]
        :rtype: int
        """
        min_len = float('inf')

        seen = {}

        for i, c in enumerate(cards):
            if not(c in seen):
                seen[c] = i
            else:
                if i - seen[c] + 1 < min_len:
                    min_len = i - seen[c] + 1
            seen[c] = i

        if min_len == float('inf'):
            return -1

        return min_len