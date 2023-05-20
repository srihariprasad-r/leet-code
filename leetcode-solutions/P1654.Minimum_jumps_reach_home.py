# wrong submission

class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        q = list()
        q.append(0)
        steps = 0

        while q:
            for _ in range(len(q)):
                el = q.pop()

                if el == x:
                    return steps

                if a + el > 0 and not(a + el in forbidden):
                    q.append(a+el)

                if el - b > 0 and not(el-b in forbidden):
                    q.append(el-b)

            steps += 1

        return steps
