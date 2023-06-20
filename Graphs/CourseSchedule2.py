class Solution:
    '''My attempt using BFS wasn't quite right.'''
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # construct prerequisite map
        preMap = {i:[] for i in range(numCourses)}
        for c, p in prerequisites:
            preMap[c].append(p)
        

        res = []

        # perform bfs
        pathFound = set()
        def bfs(crs):
            q = deque()
            q.append(crs)
            visit = set()

            while q:
                for _ in range(len(q)):
                    cur = q.popleft()

                    # terminate if loop found
                    if cur in visit:
                        return []
                    visit.add(cur)

                    # only do the following if haven't already found course path
                    if cur not in pathFound:
                        pathFound.add(cur)

                        # add to path and add prerequisites to queue
                        res.append(cur)
                        for pre in preMap[cur]:
                            q.append(pre)
        
        for c in range(numCourses):
            bfs(c)
        
        return res


class Solution:
    '''Neetcode solution using DFS'''
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {c: [] for c in range(numCourses)}
        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        output = []
        visit, cycle = set(), set()

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True

            cycle.add(crs)
            for pre in prereq[crs]:
                if dfs(pre) == False:
                    return False
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True

        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return output

        