# 54 https://leetcode.com/problems/spiral-matrix/

def spiralOrder(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    res = []
    
    r_i, r_f = 0, len(matrix)-1
    c_i, c_f = 0, len(matrix[0])-1
    
    while r_i <= r_f and c_i <= c_f:
        # right: c_i to c_f, at r_i
        for j in range(c_i, c_f+1):
            res.append(matrix[r_i][j])
        r_i += 1
        
        # down: r_i to r_f, at c_f
        for i in range(r_i, r_f+1):
            res.append(matrix[i][c_f])
        c_f -= 1
        
        # left: c_f to c_i, at r_f
        if r_i <= r_f:
            for j in reversed(range(c_i, c_f+1)):
                res.append(matrix[r_f][j])
        r_f -= 1
        
        # up: r_f to r_i, at c_i
        if c_i <= c_f:
            for i in reversed(range(r_i, r_f+1)):
                res.append(matrix[i][c_i])
        c_i += 1
    
                
    return res