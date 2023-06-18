class Solution:
    '''I couldn't figure it out.'''
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])

        def dfs(r,c):
            if r - 1 < 0:
                return set("pacific")
            if r + 1 >= rows:
                return set("atlantic")
            if c - 1 < 0:
                return set("pacific")
            if c + 1 >= cols:
                return set("atlantic")
            
            dest = set()
            dset = [[1,0], [0,1], [-1,0], [0, -1]]
            for dr, dc in dset:
                if heights[r+dr][c+dc] >= heights[r][c]:
                    dest.union(dfs(r+dr, c+dc))
            
            return dest
        
        res = []
        bing = set(["pacific", "atlantic"])
        for r in range(rows):
            for c in range(cols):
                if bing == dfs(r,c):
                    res.append([r,c])
        
        return res
    

class Solution:
    '''Neetcode solution'''
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])

        def dfs(r,c, visit, prevHeight):
            if (
                r not in range(rows) or
                c not in range(cols) or
                (r,c) in visit or
                prevHeight > heights[r][c]
            ):
                return
            
            visit.add((r,c))
            dfs(r+1,c, visit, heights[r][c])
            dfs(r-1,c, visit, heights[r][c])
            dfs(r,c+1, visit, heights[r][c])
            dfs(r,c-1, visit, heights[r][c])
        

        pac = set()
        atl = set()
        for c in range(cols):
            dfs(0, c, pac, 0)
            dfs(rows - 1, c, atl, 0)
        
        for r in range(rows):
            dfs(r, 0, pac, 0)
            dfs(r, cols - 1, atl, 0)
        
        # could probably do a union here
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        
        return res



