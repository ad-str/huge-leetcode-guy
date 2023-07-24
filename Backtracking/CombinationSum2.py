'''My assisted solution. I got 80% of the way there but needed some help from neetcode.'''
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(idx, total, combination):
            if total == 0:
                res.append(combination)
                return
            
            prev = -1
            for i in range(idx, len(candidates)):
                if candidates[i] == prev:
                    continue

                if candidates[i] <= total:
                    dfs(i+1, total - candidates[i], combination + [candidates[i]])
                prev = candidates[i]
        
        dfs(0,target, [])
        return res
