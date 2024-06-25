class Solution:
    def waysToReachStair(self, k: int) -> int:
        mp = collections.defaultdict(int)
        def combinations(m, jump, cs):            
            if (m < 0) : return 0

            if m > k + 1 : return 0

            if str(m) + "" + str(jump) + "" + str(cs) in mp:
                return mp[str(m) + "" + str(jump) + "" + str(cs)]

            steps = 0

            if m == k: steps += 1

            if cs == 0: steps += combinations(m-1, jump, cs + 1)     
            steps += combinations(m + (2 ** jump),  jump + 1, 0)

            mp[str(m) + "" + str(jump) + "" + str(cs)] = steps

            return steps

        return combinations(1, 0, False)