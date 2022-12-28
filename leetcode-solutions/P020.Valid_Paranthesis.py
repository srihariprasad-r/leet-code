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

# Method 2:

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2 : return False

        stck = []

        for c in s:
            if c in ('(', '{','['):
                stck.append(c)
            else:
                if stck:
                    el = stck.pop()
                    if not((c == ')' and el == '(') or (c == '}' and el == '{') \
                        or (c == ']' and el == '[')):
                        return False
                else:
                    return False

        return True if not stck else False
