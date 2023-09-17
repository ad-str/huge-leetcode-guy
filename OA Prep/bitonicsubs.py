def countBitonicSubsequences(arr):
    n = len(arr)
    
    # Initialize two arrays to store the count of increasing and decreasing subsequences
    increasing = [0] * n
    increasing[0] = 0

    for i in range(1, n):
        last = -1
        for j in range(i - 1, -1, -1):
            if arr[j] < arr[i]:
                last = j
                break
        if last != -1:
            increasing[i] = increasing[last] + 1
        else:
            increasing[i] = 0


    # same thing but for decreasing
    decreasing = [0] * n

    for i in range(n - 2, -1, -1):
        last = -1
        for j in range(i, n):
            if arr[j] < arr[i]:
                last = j
                break
        if last != -1:
            decreasing[i] = decreasing[last] + 1
        else:
            decreasing[i] = 0
    
    # put them together
    cou = 0
    for i in range(n):
        cou += increasing[i] * decreasing[i]
    
    return cou

if __name__ == "__main__":
    arr = [1,2,3,2,1]
    print(countBitonicSubsequences(arr))