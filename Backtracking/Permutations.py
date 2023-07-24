'''My solution. Works well enough but I feel a little queasy about the copies.'''
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []


        def dfs(visited, list):
            if len(list) == len(nums):
                res.append(list)
                return
            
            for num in nums:
                if num in visited:
                    continue
                copy = visited.copy()
                copy.add(num)
                copyl = list.copy()
                copyl.append(num)
                dfs(copy, copyl)
        
        dfs(set(), [])
        return res

'''Neetcode solution. Works by starting with the whole list and gradually deleting indices to then append
them later. Slightly more efficient than my solution.'''
class Solution2:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        # base case
        if len(nums) == 1:
            return [nums[:]]  # nums[:] is a deep copy

        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)

            for perm in perms:
                perm.append(n)
            res.extend(perms)
            nums.append(n)
        return res
