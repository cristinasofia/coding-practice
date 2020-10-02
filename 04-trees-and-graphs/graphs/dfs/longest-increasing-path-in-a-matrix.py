
def longestIncreasingPath(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: int
    """
    if not matrix:
        return 0
    
    rows = len(matrix)
    cols = len(matrix[0])
    
    def dfs(r, c):
        
        ans = 0
        
        if r-1 > 0 and matrix[r-1][c] > matrix[r][c]:
            ans = max(ans, dfs(r-1,c))
        if r+1 < rows and matrix[r+1][c] > matrix[r][c]:
            ans = max(ans, dfs(r+1,c))
        if c > 0 and matrix[r][c-1] > matrix[r][c]:
            ans = max(ans, dfs(r,c-1))
        if c+1 < cols and matrix[r][c+1] > matrix[r][c]:
            ans = max(ans, dfs(r,c+1))
        ans += 1
        return ans
    
    ans = 0
    for i in range(rows):
        for j in range(cols):
            ans = max(ans, dfs(i,j))
    
    ans += 1
    return ans