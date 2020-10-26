# 73 https://leetcode.com/problems/set-matrix-zeroes/

def setZeroes(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    
    rows = len(matrix)
    cols = len(matrix[0])
    
    # O(m+n) space
    # eliminating this would improve space complexity
    r = set()
    c = set()
    
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                r.add(i)
                c.add(j)
                
    
    for i in range(rows):
        for j in range(cols):
            if i in r or j in c:
                matrix[i][j] = 0