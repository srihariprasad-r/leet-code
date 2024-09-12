class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        n = len(piles)
        m = len(piles[0])

        def recursion(pile, idx, c):
            if idx >= m: return 0

            if c <= 0: return 0

            take_from_pile = piles[pile][idx] + recursion(pile,idx+1, c - 1)
            check_next_pile_same_idx = piles[pile][idx] + recursion(pile+1,idx, c - 1)
            not_take_from_pile = recursion(pile+1,idx+1, c - 1)

            return max(take_from_pile, max(check_next_pile_same_idx,not_take_from_pile))
        
        return recursion(0, 0, k)            