from typing import List 
import collections

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''This was my first attempt. The idea is to store the numbers into sets for each row, column, 
        and block. Then check if the current number is in any of them. I had to use some thinking to
        figure out how to mathematically indicate the current block.'''
        transposed = [set() for _ in range(len(board))] # initialize transposed set 
        blocks = [set() for _ in range(len(board))] # initialize blocks set 
        for i in range(0,len(board)):
            row = set()
            for j in range(0, len(board[0])):
                element = board[i][j]
                if element == ".":
                    continue

                if element in row or element in transposed[j] or element in blocks[3*(i//3) + j//3]:
                    return False

                row.add(board[i][j])
                transposed[j].add(board[i][j])
                blocks[3*(i//3) + j//3].add(board[i][j])
        
        return True
    
    def isValidSudoku2(self, board: List[List[str]]) -> bool:
        '''A solution I found that is a slight alteration to mine. Instead of storing the sets in lists, 
        it stores them in dictionaries which makes it simpler for the blocks since it can use a tuple for
        the key. However, it performs about the same as my solution.'''
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)  # key = (r /3, c /3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (
                    board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r // 3, c // 3)]
                ):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True

if __name__ == "__main__":
    solution = Solution() 

    board = [["8","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]
    result = solution.isValidSudoku(board)
    print(result)