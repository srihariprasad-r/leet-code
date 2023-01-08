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

# Method 2

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        lst = list(dominoes)
        d = deque()

        for i in range(len(lst)):
            if lst[i] != '.':
                d.append((i, lst[i]))

        while d:
            idx, dom = d.popleft()

            if dom == 'L':
                if idx > 0 and lst[idx-1] == '.':
                    lst[idx-1] = 'L'
                    d.append((idx-1, 'L'))
            else:
                if idx + 1 < len(lst) and lst[idx + 1] == '.':
                    if idx + 2 < len(lst) and lst[idx+2] == 'L':
                        d.popleft()
                    else:
                        lst[idx+1] = 'R'
                        d.append((idx+1, 'R'))

        return ''.join(lst)
