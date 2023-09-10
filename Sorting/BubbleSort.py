from typing import List


class Solution:
    def bubbleSort(self, arr: List) -> List:
        for i in range(len(arr) - 1, -1, -1):
            for j in range(i):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr


if __name__ == "__main__":
    s = Solution()

    print(s.bubbleSort(list(map(int, input().strip().split()))))
