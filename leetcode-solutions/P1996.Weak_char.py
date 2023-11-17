# wrong submission

class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties = sorted(properties, key=lambda x:-x[0])

        stck = [properties[0]]
        c = 0

        for i in range(1, len(properties)):
            while stck and stck[-1][1] <= properties[i][1]:
                stck.pop()
            if stck: c+= 1
            stck.append(properties[i])

        return c