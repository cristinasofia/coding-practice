# 22 https://leetcode.com/problems/generate-parentheses/
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
def generate(n):
    paren = []
    def backtrack(p, l, r):
        if r == n:
            paren.append(''.join(p))
        else:
            if l > r: # add closed parentheses
                backtrack(p + ")", l, r+1)
            if l < n: # add open parentheses
                backtrack(p + "(", l+1, r)
                
    p = ""
    backtrack(p, 0, 0)
    
    return paren
    
def generateParenthesis2(n):
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


n = 3
print(generate(n))