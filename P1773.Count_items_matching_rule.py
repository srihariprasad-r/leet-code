class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        flag = [False] * len(items)
        cnt = 0 
        
        idx = 0
        if ruleKey == 'type':
            idx = 0
        elif ruleKey == 'color':
            idx = 1
        elif ruleKey == 'name':
            idx = 2
        
        for item in range(len(items)):
            ty, col, nm = items[item]
            if idx == 0:
                if ty == ruleValue:
                    flag[item] = True
            elif idx == 1:
                if col == ruleValue:
                    flag[item] = True
            elif idx == 2:
                if nm == ruleValue:
                    flag[item] = True
                    
                    
        for i in range(len(flag)):
            if flag[i]:
                cnt += 1
            
        return cnt