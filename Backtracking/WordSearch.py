'''My solution. Had one small bug where I put the visited (i,j) inside the for loop instead of outside.'''
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        visited = set()

        def dfs(i, row, col):
            if row < 0 or row >= ROWS or col < 0 or col >= COLS:
                return False
            if (row,col) in visited:
                return False

            if board[row][col] == word[i]:
                if i == len(word) - 1:
                    return True
                
                visited.add((row,col))
                for dr, dc in [(1,0), (0,1), (-1,0), (0,-1)]:
                    if dfs(i+1, row + dr, col + dc):
                        return True
                visited.remove((row,col))
            else:
                return False
        
        for i in range(ROWS):
            for j in range(COLS):
                if dfs(0, i, j):
                    return True
        
        return False
    

'''Neetcode Solution. Has a small trick of reversing the word based on first and last letter frequency
which possibly speeds up the dfs process of finding a match.'''
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            if (
                min(r, c) < 0
                or r >= ROWS
                or c >= COLS
                or word[i] != board[r][c]
                or (r, c) in path
            ):
                return False
            path.add((r, c))
            res = (
                dfs(r + 1, c, i + 1)
                or dfs(r - 1, c, i + 1)
                or dfs(r, c + 1, i + 1)
                or dfs(r, c - 1, i + 1)
            )
            path.remove((r, c))
            return res

        # To prevent TLE,reverse the word if frequency of the first letter is more than the last letter's
        count = defaultdict(int, sum(map(Counter, board), Counter()))
        if count[word[0]] > count[word[-1]]:
            word = word[::-1]
            
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False

    # O(n * m * 4^n)