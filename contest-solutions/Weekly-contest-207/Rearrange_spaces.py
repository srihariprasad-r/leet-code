class Solution:
    def reorderSpaces(self, text: str) -> str:
        words = text.split()
        spaces = text.count(' ')
        
        if len(words) == 1:
            return words[0] + ' ' * spaces
        
        q, r = divmod(spaces, len(words)-1)
        
        return (' ' * q).join(words) + ' ' * r