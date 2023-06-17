class Solution:
    '''My attempt was correct but honestly a kind of messy way to do it.'''
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        max = 0
        temparea = 0

        rows, cols = len(grid), len(grid[0])

        def dfs(r,c):
            nonlocal temparea
            if (
                r not in range(rows) or
                c not in range(cols) or
                (r,c) in visited
            ):
                return
            
            if grid[r][c] == 1:
                visited.add((r,c))
                temparea+=1
                
                # recurse on neighbors
                dfs(r+1,c)
                dfs(r-1,c)
                dfs(r,c+1)
                dfs(r,c-1)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    dfs(r,c)
                    if temparea > max:
                        max = temparea
                    temparea = 0
        
        return max
    
class Solution:
    '''Neetcode solution doesn't use the temparea variable I had and instead returns area from the dfs'''
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()

        def dfs(r, c):
            if (
                r < 0
                or r == ROWS
                or c < 0
                or c == COLS
                or grid[r][c] == 0
                or (r, c) in visit
            ):
                return 0
            visit.add((r, c))
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

        area = 0
        for r in range(ROWS):
            for c in range(COLS):
                area = max(area, dfs(r, c))
        return area
