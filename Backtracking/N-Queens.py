from typing import List

'''My solution. Memory capacity exceeded because I had to constantly create copies since I wasn't sure
how to add then pop the added elements.'''
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        # need to find a better way to do this
        def addInvalidSquares(row, col, invalid):
            # add self
            invalid.add((row,col))

            # add horizontals and verticals:
            for j in range(n):
                invalid.add((row, j))
            for i in range(n):
                invalid.add((i, col))
            
            # add diagonals:
            for dr, dc in [(1,1), (-1,-1), (1,-1), (-1,1)]:
                i = row + dr
                j = col + dc
                while i in range(n) and j in range(n):
                    invalid.add((i,j))
                    i = i + dr
                    j = i + dc
            
            return invalid

        res = []
        def dfs(i, invalid, cur):
            if i == n:
                res.append(cur[:])

            for j in range(n):
                if (i,j) not in invalid:
                    str = "."*(i) + "Q" + "."*(n-i)
                    copy = invalid.copy()
                    addInvalidSquares(i, j, copy)
                    dfs(i+1, copy, cur+[str])

        dfs(0, set(), [])
        return res
    
'''My solution once I learned how to have a unique id for the diagonals'''
class Solution2:
    def solveNQueens(self, n: int) -> List[List[str]]:

        # need to find a better way to do this
        # col
        # positive diagonal: r + c
        # negative diagonal: r - c
        invalidCol = set()
        invalidPosDiag = set()
        invalidNegDiag = set() 

        res = []
        def dfs(i, invalid, cur):
            if i == n:
                res.append(cur[:])
                return

            for j in range(n):
                if (
                    j not in invalidCol and
                    i+j not in invalidPosDiag and
                    i-j not in invalidNegDiag
                ):
                    invalidCol.add(j)
                    invalidPosDiag.add(i+j)
                    invalidNegDiag.add(i-j)
                    
                    str = "."*(j) + "Q" + "."*(n-j-1)
                    dfs(i+1, copy, cur+[str])

                    invalidCol.remove(j)
                    invalidPosDiag.remove(i+j)
                    invalidNegDiag.remove(i-j)

        dfs(0, set(), [])
        return res
    

'''Neetcode solution'''
class Solution3:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posDiag = set()  # (r + c)
        negDiag = set()  # (r - c)

        res = []
        board = [["."] * n for i in range(n)]

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for c in range(n):
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue

                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"

                backtrack(r + 1)

                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."

        backtrack(0)
        return res
