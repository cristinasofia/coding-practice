# 48 https://leetcode.com/problems/rotate-image/

def rotate(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    
    rows = len(matrix)
    cols = len(matrix[0])
    
    # transpose
    for i in range(rows):
        for j in range(i, cols):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # reverse each row
    for i in range(rows):
        matrix[i].reverse()