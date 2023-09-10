from typing import List

'''Selection sort'''


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            # find the argmin of array[i:]
            argmin = i
            for j in range(i+1, len(nums)):
                if nums[j] < nums[argmin]:
                    argmin = j

            # swap nums[i] with the minimum value of the right array
            # tmp = nums[argmin]
            # nums[argmin] = nums[i]
            # nums[i] = tmp

            # use tuple unpacking instead
            nums[argmin], nums[i] = nums[i], nums[argmin]

        return nums


if __name__ == "__main__":
    solution = Solution()

    print(solution.sortArray(list(map(int, input().strip().split()))))