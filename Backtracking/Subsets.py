from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            for i in range(len(res)):
                copy = res[i].copy()
                copy.append(num)
                res.append(copy)
        
        return res

if __name__ == "__main__":
    sol = Solution()

    print(sol.subsets([1,2,3]))