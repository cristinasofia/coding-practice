# 1239 https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/

def maxLength(self, arr):
    """
    :type arr: List[str]
    :rtype: int
    """
    
    dp = [set()]
    max_len = 0
    
    for i in arr:
        if len(set(i)) < len(i): continue # if string has repeating characters
        a = set(i)
        for b in dp:
            if a & b: # intersection: a and b have similar characters
                continue
            max_len = max(max_len, len(a|b))
            dp.append(a | b) # union: a and b together
    
    return max_len