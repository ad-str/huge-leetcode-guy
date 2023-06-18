class Solution:
    '''My attempt: I tried to do a separates bfs for each rotten orange and return the max time but I
    didn't realize that I can do a bfs with all of them simultaneously and just alter the grid directly
    to determine how many fresh fruit is still left.'''
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        rottensVisited = set()

        def bfs(startRow, startCol, minutes):
            q = deque()
            q.append((startRow, startCol))
            visit = set()

            while q:
                r,c = q.popleft()
                visit.add((r,c))
                delta = [[1,0], [0,1], [-1,0], [0,-1]]
                for dr, dc in delta:
                    if grid[r+dr][c+dc] == 1 and (r+dr, c+dc) not in visit:
                        q.append((r+dr, c+dc))
                
                minutes += 1
            
            return minutes
        
        res = -1
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2 and (r,c) not in rottensVisited:
                    rottensVisited.add((r,c))
                    res = max(res, bfs(r,c, 0))

        for r in range(rows):
            for c in range(cols):
                if (r,c) != 0 and (r,c) not in visit:
                    return -1

        return res



        
