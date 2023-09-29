def maxSumSubSquare(matrix: list, k: int) -> list:
    '''
    Key idea is to preprocess the matrix by storing sums of strips
    of length k
    '''
    m = len(matrix)
    n = len(matrix[0])
    sumStrips = [[0] * n for _ in range(m - k + 1)]

    for j in range(n):
        # get the sum of the first strip for this column
        for i in range(k):
            sumStrips[0][j] += matrix[i][j]

        # get the sum of the rest of the strips
        for i in range(1, n - k + 1):
            sumStrips[i][j] = sumStrips[i - 1][j] + (
                matrix[i + k - 1][j] - matrix[i - 1][j]
            )
    
    # now compute the sum of the first submatrix
    # which sums the first k strips in the first row
    sumSubSquare = [[0] * (n - k + 1) for _ in range((m - k + 1))]

    # row by row
    for i in range(m - k + 1):
        # first subsquare
        for j in range(k):
            sumSubSquare[i][j] += sumStrips[i][j]
        
        # next subsquares in this row
        for j in range(1, n - k + 1):
            sumSubSquare[i][j] = sumSubSquare[i][j - 1] + (
                sumStrips[i][j + k - 1] - sumStrips[i][j - 1]
            )
    
    return sumSubSquare

if __name__ == "__main__":
    mat = [[1, 1, 1, 1, 1],
       [2, 2, 2, 2, 2],
       [3, 3, 3, 3, 3],
       [4, 4, 4, 4, 4],
       [5, 5, 5, 5, 5]]
    k = 3

    print(maxSumSubSquare(mat, k))