class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        stck = []
        for i in range(len(S)):
            if stck and stck[-1] == S[i]:
                stck.pop()
            else:
                stck.append(S[i])

        return "".join(stck)