'''My solution passes but is inefficient. It is inspired by Bellman-Ford. O(mnlog(mn)). Faster to just do brute force DFS at each cell
with memoization which I definitely didn't think was possible lol even though I thought of it.'''
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        prev = [[True] * len(matrix[0]) for _ in range(len(matrix))]
        res = 1

        for _ in range(len(matrix) * len(matrix[0])):
            new = [[False] * len(matrix[0]) for _ in range(len(matrix))]
            found = False
            for i in range(len(prev)):
                for j in range(len(prev[0])):
                    if prev[i][j]==False:
                        continue
                    else:
                        for dr, dc in [[1,0], [-1,0], [0,1], [0,-1]]:
                            if (
                                i + dr >= 0 and
                                j + dc >=0 and
                                i + dr < len(prev) and
                                j + dc < len(prev[0]) and
                                prev[i+dr][j+dc]
                            ):
                                if matrix[i][j] > matrix[i+dr][j+dc]:
                                    new[i][j] = True
                                    found = True
            
            prev = new
            if found:
                res += 1
            else:
                break
        
        return res
    
'''Neetcode solution'''
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = {}  # (r, c) -> LIP

        def dfs(r, c, prevVal):
            if r < 0 or r == ROWS or c < 0 or c == COLS or matrix[r][c] <= prevVal:
                return 0
            if (r, c) in dp:
                return dp[(r, c)]

            res = 1
            res = max(res, 1 + dfs(r + 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r - 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r, c + 1, matrix[r][c]))
            res = max(res, 1 + dfs(r, c - 1, matrix[r][c]))
            dp[(r, c)] = res
            return res

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, -1)
        return max(dp.values())
