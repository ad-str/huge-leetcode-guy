from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(subcandidates, total, cur):
            # base case when the remainder is 0 -> means we have found a sum
            if total == 0:
                res.append(cur)
                return
            
            # iterate over children
            for i in range(len(subcandidates)):
                if subcandidates[i] <= total:
                    # perform a dfs on the remainder using itself and candidates to the right
                    dfs(subcandidates[i:], total - subcandidates[i], cur + [subcandidates[i]])
        
        
        dfs(candidates, target, [])

        return res
    
if __name__ == "__main__":
    sol = Solution()

    print(sol.combinationSum([2,3,5], 8))