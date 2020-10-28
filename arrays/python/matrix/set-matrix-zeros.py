# 73 https://leetcode.com/problems/set-matrix-zeroes/

def setZeroes(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    
    rows = len(matrix)
    cols = len(matrix[0])
    
    visited = set()
    
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                visited.add(i)
                visited.add(j)
                
    
    for i in range(rows):
        for j in range(cols):
            if i in visited or j in visited:
                matrix[i][j] = 0

    print matrix