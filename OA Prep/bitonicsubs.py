def countBitonicSubsequences(arr):
    n = len(arr)
    
    # dpi[i] represent the number of increasing subsequences that end at dpi[i]
    dpi = [0] * len(arr)

    for i in range(1, len(arr)):
        for j in range(0, i):
            if arr[j] < arr[i]:
                dpi[i] += dpi[j] + 1 # plus 1 to account for new {j, i} subsequence


    # dpd[i] represents the number of decreasing subsequences that start at dpd[i]
    dpd = [0] * len(arr)

    for i in range(len(arr) - 2, -1, -1):
        for j in range(len(arr) - 1, i, -1):
            if arr[j] < arr[i]:
                dpd[i] += dpd[j] + 1 # plus 1 to account for new {i, j} subsequence
    
    # put them together
    cou = 0
    for i in range(n):
        cou += dpi[i] * dpd[i]
    
    return cou

def countIncreasingSubsequences(arr):
    # dp[i] represents the number of strictly increasing subsequences
    # that end with dp[i]. Must have at least 2 elements.
    dp = [0] * len(arr)

    for i in range(1, len(arr)):
        for j in range(0, i):
            if arr[j] < arr[i]:
                dp[i] += dp[j] + 1 # plus 1 to account for new {j, i} subsequence
    
    print(dp)
    return sum(dp)

def countDecreasingSubsequences(arr):
    # dp[i] represents the number of strictly decreasing subsequences
    # that start with dp[i]. Must have at least 2 elements
    dp = [0] * len(arr)

    for i in range(len(arr) - 2, -1, -1):
        for j in range(len(arr) - 1, i, -1):
            if arr[j] < arr[i]:
                dp[i] += dp[j] + 1 # plus 1 to account for new {i, j} subsequence
    
    print(dp)
    return sum(dp)

if __name__ == "__main__":
    arr = [1,2,3,2,4]
    print(arr)
    print(countIncreasingSubsequences(arr))
    print(countDecreasingSubsequences(arr))
    print(countBitonicSubsequences(arr))