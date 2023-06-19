class Solution:
    '''I could not figure this out on my own. I did know that the algorithm should return false if 
    there is a directed cycle. I also wrote out a map representing the graph and even drew arrows 
    representing a dfs algorithm to determine if there is a cycle. However, I felt like it wasn't 
    fast enough since we'd have to perform a dfs on each course number so potentially n^2 time but the
    neetcode solution ends up doing just that. So I guess it's fine?'''
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # dfs
        preMap = {i: [] for i in range(numCourses)}

        # map each course to : prereq list
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visiting = set()

        def dfs(crs):
            if crs in visiting:
                return False
            if preMap[crs] == []:
                return True

            visiting.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            preMap[crs] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
