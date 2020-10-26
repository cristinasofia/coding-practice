
def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    
    d = {')':'(', ']':'[','}':'{'}
    
    stack = []
    
    for i in s:
        if i in d:
            if stack.pop() != d[i]:
                return False
        else:
            stack.append(i)
    
    return len(stack) == 0