'''My original solution. Got it within like 10 minutes. O(mn) time and O(m+n) space'''
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        rows = set()
        cols = set()

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in rows or j in cols:
                    matrix[i][j] = 0
        
        return matrix
    
'''Looked up other solutions to see if there was a solution with smaller space complexity. This implementation is O(1) space 
complexity but for some reason is larger space than my previous implementation according to leetcode'''
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        col0 = False

        for i in range(len(matrix)):
            if matrix[i][0] == 0: col0 = True
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(len(matrix) - 1 , -1 , -1):
            for j in range(len(matrix[0]) - 1, 0, -1):
                if (matrix[i][0] == 0 or matrix[0][j] == 0):
                    matrix[i][j] = 0
            if col0: matrix[i][0] = 0
        
        return matrix