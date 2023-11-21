class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        from bisect import bisect_left
        potions.sort()
        
        res = [0] * len(spells)

        for idx, num in enumerate(spells):
            m = success/num
            res[idx] = len(potions) - bisect_left(potions, m)

        return res