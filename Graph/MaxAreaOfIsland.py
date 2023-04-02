def maxAreaOfIsland(grid) -> int:
    ROWS, COLS = len(grid), len(grid[0])
    res = 0

    def dfs(r, c) -> int:
        if (r >= ROWS or c >= COLS or r < 0 or c < 0 or grid[r][c] == 0):
            return 0
        grid[r][c] = 0
        return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

    for i in range(ROWS):
        for j in range(COLS):
            if grid[i][j] == 1:
                res = max(res, dfs(i, j))
    return res

'''
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
'''