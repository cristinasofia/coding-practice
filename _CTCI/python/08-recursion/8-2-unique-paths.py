# 62 https://leetcode.com/problems/unique-paths/
# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
# How many possible unique paths are there?

def uniquePaths(m, n):
    rows = m
    cols = n

    dp = [[1 for _ in range(cols)] for _ in range(rows)]

    for i in range(1, rows):
        for j in range(1, cols):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    return dp[rows-1][cols-1]

# 63 https://leetcode.com/problems/unique-paths-ii/
# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
# Now consider if some obstacles are added to the grids. How many unique paths would there be?

def uniquePathWithObstacles(grid):
    if grid[0][0] == 1:
        return 0
    
    rows = len(grid)
    cols = len(grid[0])

    dp = [[0 for _ in range(cols)] for _ in range(rows)]

    dp[0][0] = 1
    
    # across top row
    # if no obstacle in grid and there was a path in previous cell to the left, then 1
    for i in range(1, rows):
        dp[i][0] = 1 if grid[i][0] == 0 and dp[i-1][0] else 0

    # across first column
    # if no obstacle and there was a path in previous cell above, then 1    
    for j in range(1, cols):  
        dp[0][j] = 1 if grid[0][j] == 0 and dp[0][j-1] else 0
    
    # if no obstacles, then calculate
    for i in range(1, rows):
        for j in range(1, cols):
            if grid[i][j] == 0:    
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    return dp[rows-1][cols-1]



m, n = 3, 7
print(uniquePaths(m, n))

grid = [
    [0,0,0],
    [0,1,0],
    [0,0,0]
    ]

print(uniquePathWithObstacles(grid))