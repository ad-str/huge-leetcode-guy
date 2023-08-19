'''My original solution and it works and is decently efficient.'''
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """


        i, r = 0, len(matrix) - 1
        while i < r//2 + 1:
            for j in range(i, r - i):
                prev = matrix[i][j]
                for tr, tc in [(j,r - i), (r - i,r - j), (r - j,i), (i,j)]:
                    tmp = matrix[tr][tc]
                    matrix[tr][tc] = prev
                    prev = tmp
            i+=1

'''Neetcode solution is the same idea but slightly different implementation'''
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l, r = 0, len(matrix) - 1
        while l < r:
            for i in range(r - l):
                top, bottom = l, r

                # save the topleft
                topLeft = matrix[top][l + i]

                # move bottom left into top left
                matrix[top][l + i] = matrix[bottom - i][l]

                # move bottom right into bottom left
                matrix[bottom - i][l] = matrix[bottom][r - i]

                # move top right into bottom right
                matrix[bottom][r - i] = matrix[top + i][r]

                # move top left into top right
                matrix[top + i][r] = topLeft
            r -= 1
            l += 1