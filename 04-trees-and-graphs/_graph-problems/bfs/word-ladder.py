class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        
        import collections
        d = collections.Counter()
        chars = set(w for word in wordList for w in word)
        w_List = set(wordList)
        
        q = [[beginWord,1]]
        while q:
            w, l = q.pop(0)
            
            if w == endWord:
                return l
            
            for i in range(len(w)):
                for c in chars:
                    x = w[:i] + c + w[i+1:]
                    if x in w_List:
                        w_List.remove(x)
                        q.append([x, l + 1])
        
        
        
        return 0