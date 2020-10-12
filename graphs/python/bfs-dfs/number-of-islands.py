
def numIslands_DFS(grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    
    if not grid:
        return 0
    
    rows = len(grid)
    cols = len(grid[0])
    
    visit = [[0 for _ in range(cols)] for _ in range(rows)]
    
    def dfs(i, j):
        if i < 0 or j < 0 or i >= rows or j >= cols:
            return
        if grid[i][j] == '0' or visit[i][j]:
            return
        
        visit[i][j] = 1
        dfs(i+1,j)
        dfs(i-1, j)
        dfs(i, j+1)
        dfs(i, j-1)
    
    count = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '1' and not visit[i][j]:
                dfs(i, j)
                count += 1
            
    return count

def numIslands_BFS(grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    
    if not grid:
        return 0
    
    rows = len(grid)
    cols = len(grid[0])
    
    visit = [[0 for _ in range(cols)] for _ in range(rows)]
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    
    count = 0
    q = []
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '1' and not visit[i][j]:
                q.append((i, j))
                while q:
                    x, y = q.pop(0)
                    visit[x][y] = 1
                    for dx, dy in directions:
                        xx, yy = x + dx, y + dy
                        
                        if xx < 0 or yy < 0 or xx >= rows or yy >= cols:
                            continue
                        if grid[xx][yy] == '0' or visit[xx][yy]:
                            continue
                            
                        visit[xx][yy] = 1
                        q.append((xx,yy))
                    
                count += 1
                
            
    return count