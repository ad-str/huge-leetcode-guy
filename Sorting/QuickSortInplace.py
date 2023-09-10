# Enter your code here. Read input from STDIN. Print output to STDOUT
def quicksort(arr, i, j):
    # base case when we are considering subarray with less than 2 elements
    if i >= j:
        return
    
    # pick last element to be the pivot: p = arr[j]
    # initialize r to the be index for where the right subarray starts
    r = i
    for k in range(i, j):
        if arr[k] < arr[j]:
            # if lesser, swap with first element of right subarray and increment starting index of right subarray
            arr[k], arr[r] = arr[r], arr[k]
            r += 1
    # now swap pivot with the first element of right subarray
    arr[j], arr[r] = arr[r], arr[j]
    
    # recurse on left and right subarrays, not including the pivot which is in the correct place now
    quicksort(arr, i, r-1)
    quicksort(arr, r+1, j)

if __name__ == "__main__":
    arr = [1, 3, 9, 8, 2, 7, 5]
    quicksort(arr, 0, len(arr)-1)
    print(arr)