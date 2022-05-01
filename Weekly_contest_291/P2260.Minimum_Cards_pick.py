# TLE submission

class Solution(object):
    def minimumCardPickup(self, cards):
        """
        :type cards: List[int]
        :rtype: int
        """
        mp = {}

        for c in cards:
            if not(c in mp):
                mp[c] = 1
            elif c in mp:
                mp[c] += 1

        dups_flag = False
        dups_value = []
        for k, v in mp.items():
            if v >= 2:
                if not dups_flag:
                    dups_flag = True
                dups_value.append(k)

        if not dups_flag:
            return -1

        el_occurance = {}

        for v in dups_value:
            idx = 0
            while idx < len(cards):
                if cards[idx] == v:
                    el_occurance.setdefault(v, []).append(idx)
                idx += 1

        min_len = float('inf')

        for k, v in el_occurance.items():
            for i in range(len(v)-1):
                for j in range(i+1, len(v)):
                    min_len = min(min_len, v[j] - v[i] + 1)

        return min_len
