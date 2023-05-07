'''
Restriction: O(n) time and without using division operator
'''

from typing import List 

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''This was my first attempt. I realized that for each index we just need to return the product of
        elements to the left of it and to the right of it. So this algorithm works by storing the product
        of all elements in two arrays by moving from the start and end.'''
        n = len(nums)
        prodLeft, prodRight = [1]*(n+1), [1]*(n+1) # ongoing product starting from the left and right of the array

        # the use of n+1 is so that the first element stays 1
        for i in range(0, n):
            prodLeft[i+1] = prodLeft[i] * nums[i] # product from the left
            prodRight[i+1] = prodRight[i] * nums[n-1-i] # product from the right

        return [prodLeft[i]*prodRight[n-i-1] for i in range(0,n)]
    
    def productExceptSelf2(self, nums: List[int]) -> List[int]:
        '''This is a solution I found that essentially is the same idea as mine but they do it without
        storing the products in two arrays and instead just store the products from the left and then
        iterate again and multiply the products from the right'''
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res



if __name__ == "__main__":
    solution = Solution() 

    result = solution.productExceptSelf([-1,1,0,-3,3])
    print(result)