def ladderLength(beginWord, endWord, wordList):
    """
    :type beginWord: str
    :type endWord: str
    :type wordList: List[str]
    :rtype: int
    """
    import string
    q = [[beginWord,1]]
    while q:
        w, l = q.pop(0)
        
        if w == endWord:
            return l
        
        for i in range(len(w)):
            for c in string.ascii_lowercase:
                x = w[:i] + c + w[i+1:]
                if x in wordList:
                    wordList.remove(x)
                    q.append([x, l + 1])    
    
    return 0

def ladderLength_optimized(beginWord, endWord, wordList):
    
    chars = set(w for word in wordList for w in word)
    
    q = [[beginWord,1]]
    while q:
        w, l = q.pop(0)
        
        if w == endWord:
            return l
        
        for i in range(len(w)):
            for c in chars:
                x = w[:i] + c + w[i+1:]
                if x in wordList:
                    wordList.remove(x)
                    q.append([x, l + 1])
    
    
    
    return 0