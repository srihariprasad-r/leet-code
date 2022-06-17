class Solution(object):
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        leftIndex = [-1] * len(dominoes)
        rightIndex = [-1] * len(dominoes)
        ans = ['.'] * len(dominoes)

        n = len(dominoes)
        i = n - 1
        j = 0

        lIndex = -1
        while i > -1:
            if dominoes[i] == 'L':
                lIndex = i
            elif dominoes[i] == 'R':
                lIndex = -1
            leftIndex[i] = lIndex

            i -= 1

        rIndex = -1
        while j < n:
            if dominoes[j] == 'R':
                rIndex = j
            elif dominoes[j] == 'L':
                rIndex = -1
            rightIndex[j] = rIndex
            j += 1

        for i in range(n):
            if dominoes[i] != '.':
                ans[i] = dominoes[i]
            else:
                lft = leftIndex[i]
                rght = rightIndex[i]

                if lft == -1:
                    ldiff = float('inf')
                else:
                    ldiff = abs(lft - i)

                if rght == -1:
                    rdiff = float('inf')
                else:
                    rdiff = abs(rght - i)

                if ldiff == rdiff:
                    ans[i] == '.'
                elif ldiff > rdiff:
                    ans[i] = 'R'
                else:
                    ans[i] = 'L'

        return ''.join(ans)
