class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if (len(s) %2 != 0):
            return False
    
        stack_list = []
        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack_list.append(i)
            elif (i == ')' and len(stack_list) > 0 and stack_list[-1] == '('):
                stack_list.pop()
            elif (i == '}' and len(stack_list) > 0 and stack_list[-1] == '{'):
                stack_list.pop()            
            elif (i == ']' and len(stack_list) > 0 and stack_list[-1] == '['):
                stack_list.pop()             
    
        return not stack_list