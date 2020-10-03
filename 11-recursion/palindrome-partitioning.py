
def partition(s):
    """
    :type s: str
    :rtype: List[List[str]]
    """
    
    def isPalindrome(s):
        return s == s[::-1]
    
    
    def backtrack(s, path):
        if len(s) == 0:
            output.append(path)
        else:
            for i in range(1, len(s)+1):
                if isPalindrome(s[:i]):
                    backtrack(s[i:], path + [s[:i]])

    
    output = []
    backtrack(s, [])
    return output