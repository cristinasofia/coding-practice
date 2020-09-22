class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        if not grid:
            return 0
            
        fresh = 0
        import collections
        rotten = collections.deque()
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    rotten.append((i,j))
                if grid[i][j] == 1:
                    fresh += 1
        
        minutes = 0
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        
        while rotten and fresh > 0:
            minutes += 1
            
            for _ in range(len(rotten)):
                x, y = rotten.popleft()
                for dx, dy in directions:
                    xx, yy = x + dx, y + dy

                    if xx < 0 or yy < 0 or xx >= len(grid) or yy >= len(grid[0]):
                        continue
                    if grid[xx][yy] == 0 or grid[xx][yy] == 2:
                        continue

                    #if grid[xx][yy] == 1:
                    grid[xx][yy] = 2
                    fresh -= 1
                    rotten.append((xx, yy))
                    
                
        
        return minutes if minutes > 0 else -1