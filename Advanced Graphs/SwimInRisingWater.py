
'''My dumb solution. I psyched myself out thinking I couldn't use Dijkstra's because it's not cumulative
path cost but rather max cell on a given path. So I did the brute force method of trying all paths to 
bottom right. Works but inefficient.'''
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        res = float("inf")
        visit = set()

        def dfs(max, i, j):
            nonlocal res

            if (
                i < 0 or j < 0 or
                i >= n or j >= n or
                (i,j) in visit
            ):
                return
            
            if grid[i][j] > max:
                max = grid[i][j]

            if (i,j) == (n-1, n-1):
                if max < res:
                    res = max
                return
            
            visit.add((i,j))
            adj = [[1,0], [-1,0], [0,1], [0,-1]]
            for di, dj in adj:
                dfs(max, i + di, j + dj)
            visit.remove((i,j))
        
        dfs(0, 0, 0)
        return res
    
'''Reattempt after having skimmed some solutions using Dijkstra's. Works'''
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        heap = [[grid[0][0], 0, 0]]
        visit = set()

        while heap:
            w, i, j = heapq.heappop(heap)

            if i==n-1 and j == n-1:
                return w

            for ii, jj in [[i+1,j], [i-1,j], [i,j+1], [i,j-1]]:
                if 0 <= ii < n and 0 <= jj < n and (ii,jj) not in visit:
                    heapq.heappush(heap, [max(w, grid[ii][jj]), ii, jj])
                    visit.add((ii,jj))

