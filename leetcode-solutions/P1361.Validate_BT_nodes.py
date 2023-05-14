# wrong submission

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        q = list()
        q.append(0)
        seen = set()
        seen.add(0)

        while q:
            for _ in range(len(q)):
                el = q.pop()

                l = leftChild[el]
                if l >= 0:
                    if l not in seen:
                        seen.add(l)
                    else:
                        return False

                r = rightChild[el]
                if r >= 0:
                    if r not in seen:
                        seen.add(r)
                    else:
                        return False

                if el + 1 < n:
                    q.append(el+1)

        return len(seen) == n