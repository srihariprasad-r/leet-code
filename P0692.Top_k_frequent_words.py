class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        res = []
        words_dict = Counter(words)
        wordlist = [(-val,key) for key,val in words_dict.items()]
        
        heapq.heapify(wordlist)
        for i in range(k):
            res.append(heapq.heappop(wordlist)[1])
        
        return res