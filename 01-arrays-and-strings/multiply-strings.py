def multiply(self, num1, num2):
    """
    :type num1: str
    :type num2: str
    :rtype: str
    """
    
    product = [0] * (len(num1)+len(num2))
    n = len(product) -1
    
    for a in reversed(num1):
        i = n
        for b in reversed(num2):
            product[i] += int(a)*int(b)
            product[i-1] += product[i]/10
            product[i] %= 10
            i -= 1
        n -= 1
        
    pt = 0
    while pt < len(product) - 1 and product[pt] == 0:
        pt += 1
        
    return ''.join(map(str, product[pt:]))