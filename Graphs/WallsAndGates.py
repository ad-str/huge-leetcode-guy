from typing import (
    List,
)

class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """

    '''My solution. Couldn't run it on lintcode since I don't have an account but the idea looks correct.'''
    def walls_and_gates(self, rooms: List[List[int]]):
        # write your code here
        rows, cols = len(rooms), len(rooms[0])
        q = collections.deque()
        emptyRooms = 0
        dist = 0

        for r in len(rows):
            for c in len(cols):
                if rooms[r][c] == 0:
                    q.append((r,c))
                if rooms[r][c] == float("infinity"):
                    emptyRooms += 1
        
        while emptyRooms > 0 and q:
            dist += 1
            for _ in range(len(q)):
                directions = [[1,0], [-1,0], [0,1], [0,-1]]
                for dr, dc in directions:
                    row = r+dr
                    col = c+dc 

                    if (
                        row in range(rows) and
                        col in range(cols) and
                        rooms[row][col] == float("infinity")
                    ):
                        emptyRooms -= 1
                        rooms[row][col] = dist 
                        q.append((row,col))
        
        return rooms 



