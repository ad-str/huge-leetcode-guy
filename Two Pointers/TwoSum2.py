from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''To be honest I did not think this would work haha. But yes this was my first attempt. And
        I got it done in less than 25 min which is my best time so far. I came up with the algorithm
        using some scratch paper and using the fact that the array is sorted to my advantage. If I add
        two numbers right next to each other together and it is above the target, I know I can just
        move one index back and I will get a smaller sum and vice versa.'''
        i = 0
        j = 1

        firstPass = True

        while True:
            sum = numbers[i] + numbers[j]
            if sum == target: return [i+1, j+1]

            if sum > target:
                firstPass = False
                i-=1
            elif firstPass:
                i+=1
                j+=1
            elif sum < target:
                j+=1

    def twoSum2(self, numbers: List[int], target: int) -> List[int]:
        '''Here is a solution I found. It is a much more understandable version of my algorithm. I'm not
        sure why my brain thought my method was more intuitive haha. But yea this makes sense. If you add
        the left and right, if the sum is bigger than the target, decrease the right, otherwise increase
        the left. Much simpler to understand.'''
        l, r = 0, len(numbers) - 1

        while l < r:
            curSum = numbers[l] + numbers[r]

            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l + 1, r + 1]


    

if __name__ == "__main__":
    solution = Solution()

    result = solution.twoSum([2,7,11,15], 22)
    print(result)