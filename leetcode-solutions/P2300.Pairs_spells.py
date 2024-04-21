class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        from bisect import bisect_left
        potions.sort()
        
        res = [0] * len(spells)

        for idx, num in enumerate(spells):
            m = success/num
            res[idx] = len(potions) - bisect_left(potions, m)

        return res

# wrong submission
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        
        def bs(x):
            l = -1
            r = len(potions)

            while l < r:
                mid = l + (r-l)//2

                if x * potions[mid] >= success:
                    r = mid
                else:
                    l = mid + 1

            return len(potions)-l if l >= 0 else 0

        ar = []
        for a in spells:
            res = bs(a)
            ar.append(res)

        return ar