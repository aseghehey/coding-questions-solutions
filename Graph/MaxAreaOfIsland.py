def maxAreaOfIsland(self, grid) -> int:
    R, C = len(grid), len(grid[0])
    result = 0
    
    visit = set()
    
    def bfs(r, c):
        queue = [[r,c]]
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        count = 0
        visit.add((r,c))
        
        while queue:
            r, c = queue.pop(0)
            count += 1
            for v, h in directions:
                if r + v >= R or c + h >= C or r + v < 0 or c + h < 0 or (r + v, c + h) in visit or grid[r + v][c + h] == 0:
                    continue
                    
                queue.append([r + v, c + h])
                visit.add((r + v, c + h))
                    
        return count
    
    for i in range(R):
        for j in range(C):
            if grid[i][j] == 1 and (i, j) not in visit:
                result = max(result, bfs(i, j))
    return result