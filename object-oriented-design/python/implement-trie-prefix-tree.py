class Node(object):
    def __init__(self):
        self.children = [None] * 26
        self.is_end_of_word = False

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    # returns an integer representing the Unicode character
    def char_to_index(self, ch):
        return ord(ch) - ord('a')
        
    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        crawl = self.root
        for w in word:
            index = self.char_to_index(w)
            if not crawl.children[index]:
                crawl.children[index] = Node()
            crawl = crawl.children[index]
            
        crawl.is_end_of_word = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        crawl = self.root
        for w in word:
            index = self.char_to_index(w)
            if not crawl.children[index]:
                return False
            crawl = crawl.children[index]
            
        return crawl and crawl.is_end_of_word
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        crawl = self.root
        for p in prefix:
            index = self.char_to_index(p)
            if not crawl.children[index]:
                return False
            crawl = crawl.children[index]
        
        return True