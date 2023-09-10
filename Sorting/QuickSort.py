# Enter your code here. Read input from STDIN. Print output to STDOUT
def quicksort(arr):
    # step 0 base case
    if len(arr) <= 1:
        return arr

    # step 1 divide
    left, right = [], []
    for i in range(1, len(arr)):
        if arr[i] < arr[0]:
            left.append(arr[i])
        else:
            right.append(arr[i])

    # step 2 conquer - at first, I was trying to append to the sorted left array but I forgot that the append method modifies 
    # in-place and returns none, so I need to actually return a copy using + operator
    # res = quicksort(left).append(arr[0]) + quicksort(right)
    res = quicksort(left) + [arr[0]] + quicksort(right)
    print(*res)
    return res


if __name__ == "__main__":
    # n = int(input())
    # arr = list(map(int, input().strip().split()))
    arr = [5, 8, 1, 3, 7, 9, 2]

    quicksort(arr)
