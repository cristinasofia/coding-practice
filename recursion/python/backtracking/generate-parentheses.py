# 22 https://leetcode.com/problems/generate-parentheses/

def generateParenthesis(n):
    """
    :type n: int
    :rtype: List[str]
    """
    
    paren = []
    def backtrack(p, l, r):
        if l == 0 and r == 0:
            paren.append(''.join(p))
        else:
            if l != 0:
                backtrack(p + "(", l - 1, r)
            if r > l:
                backtrack(p + ")", l, r - 1)
                
            
            
    p = ""   
    backtrack(p, n, n)
    
    return paren