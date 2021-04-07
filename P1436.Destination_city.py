class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        way = set()
        
        for path in paths:
            way.add(path[1])
        
        for path in paths:
            if path[0] in way:
                way.remove(path[0])
            
        return ''.join(way)