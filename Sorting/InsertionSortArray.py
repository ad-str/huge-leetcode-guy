'''This was done on Hackerrank. It basically copies elements at index i-1 to i and eventually inserts the number to sort'''
def insertionSort2(n, arr):
    
    for i in range(1, len(arr)):
        num = arr[i]
        c = i
        while c > 0 and arr[c-1] > num:
            arr[c] = arr[c-1]
            c -= 1
        arr[c] = num
        
        print(*arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)