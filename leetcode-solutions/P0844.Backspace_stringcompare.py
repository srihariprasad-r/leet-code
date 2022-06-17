class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        stck_S = []
        stck_T = []
    
        j = 0
        while j < len(S):
            if S[j] != '#':
                stck_S.append(S[j])
            else:
                if len(stck_S) > 0: stck_S.pop()
            j += 1

        j = 0
        while j < len(T):
            if T[j] != '#':
                stck_T.append(T[j])
            else:
                if len(stck_T) > 0: stck_T.pop()
            j += 1
    
        return True if "".join(stck_S) == "".join(stck_T) else False