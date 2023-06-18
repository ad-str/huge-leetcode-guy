class Solution:
    '''My solution. I noticed it was pretty much similar to the pacific atlantic flow problem since
    a region can be safe only if one of its nodes is at the edge.'''
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        rows, cols = len(board), len(board[0])
        safe = set()
        
        def dfs(r,c):
            if (
                r not in range(rows) or 
                c not in range(cols) or
                (r,c) in safe or
                board[r][c] == "X"
            ):
                return
            
            safe.add((r,c))
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        
        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols-1)
        
        for c in range(cols):
            dfs(0, c)
            dfs(rows-1, c)
        

        for r in range(rows):
            for c in range(cols):
                if (r,c) not in safe and board[r][c] == "O":
                    board[r][c] = "X"
        