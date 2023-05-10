from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''My first attempt does not work. I went down a rabbit hole of one algorithm I came up with just
        to realize it's O(n^3) anyway... Will need to revisit this...'''
        result = []
        l = 0
        r = len(nums) - 1

        nums.sort()

        while nums[l] <= 0 and nums[r] >= 0:
            twosum = nums[l] + nums[j]

            if twosum > nums[r]:
                l += 1
                j = r
                continue
            elif twosum < nums[l]:
                r -= 1
                j = r
                continue
            
            need = 0 - twosum

            for k in range(l+1, r):
                if nums[k] == need:
                    result.append([nums[l], nums[k], nums[r]])
                    break
            
            j -= 1
        return False

    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        '''I reviewed a solution I found earlier in the day and came back to it to attempt this problem
        again from what I remembered. I was able to remember the solution pretty well and it makes sense'''
        nums.sort()

        result = []

        for index in range(len(nums)):

            # I forgot this part
            if nums[index] > 0:
                break # no way for it to sum to 0
            if index > 0 and nums[index] == nums[index - 1]:
                continue # deal with duplicate in for loop


            l, r = index + 1, len(nums) - 1

            while l < r:
                if nums[index] + nums[l] + nums[r] < 0:
                    # if this is the case, we need the sum of left and right to be bigger
                    l+=1
                elif nums[index] + nums[l] + nums[r] > 0:
                    # need l + r to be smaller
                    r-=1
                else:
                    # it is equal
                    result.append([nums[index], nums[l], nums[r]])
                    # iterate both left and right instead of just one since you know the sum will not
                    # add up to 0 if one is a different number
                    l+=1
                    r-=1
                    # deal with duplicates in while loop
                    while nums[l] == nums[l - 1] and l < r:
                        l+=1
        return result



if __name__ == "__main__":
    solution = Solution() 

    result = solution.threeSum([-1,0,1,2,-1,-4])
                