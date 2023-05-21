from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''Here's what I came up with'''
        m = len(matrix)
        n = len(matrix[0])

        l = 0
        r = m * n - 1

        while l <= r:
            mid = (l + r) // 2

            if target < matrix[mid // n][mid % n]:
                r = mid - 1
            elif target > matrix[mid // n][mid % n]:
                l = mid + 1
            else:
                return True
        
        return False
    

if __name__ == "__main__":
    solution = Solution()

    solution.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 5)