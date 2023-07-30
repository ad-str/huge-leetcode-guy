from typing import List
from collections import defaultdict

class Solution2:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(reverse = True, key = lambda x: x[1])

        # make adjacency list
        graph = defaultdict(list)
        for edge in tickets:
            graph[edge[0]].append(edge[1])
        
        res = ["JFK"]
        for i in range(len(tickets)):
            dest = graph[res[i]].pop()
            res.append(dest)
        
        return res

class Solution3:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(key = lambda x: x[1])

        # make adjacency list with lexicographic order of neighbors
        graph = defaultdict(list)
        for edge in tickets:
            graph[edge[0]].append(edge[1])

        visited = set()
        res = []
        def dfs(vertex, cur):
            if len(visited) == len(tickets):
                res.append(cur)
                return True
            
            for nei in graph[vertex]:
                if (vertex, nei) in visited:
                    continue
                
                visited.add((vertex, nei))
                if dfs(nei, cur+[nei]):
                    return True
                visited.remove((vertex, nei))
            
            return False

        dfs("JFK", ["JFK"])
        return res

'''My solution assumes that edges are unique. I.e. JFK -> ANU can only happen once. But the problem
assumes it can happen any number of times. So a visited edge set won't work. Need to go back to
popping neighbors in the adjacency list.'''
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(key = lambda x: x[1])

        # make adjacency list with lexicographic order of neighbors
        graph = defaultdict(list)
        for edge in tickets:
            graph[edge[0]].append(edge[1])

        visited = set()
        def dfs(vertex, cur):
            if len(visited) == len(tickets):
                return cur
            
            for nei in graph[vertex]:
                if (vertex, nei) in visited:
                    continue
                
                visited.add((vertex, nei))
                val = dfs(nei, cur+[nei])
                if val:
                    return val
                visited.remove((vertex, nei))

        return dfs("JFK", ["JFK"])
        
'''Neetcode solution. I have basicaly the same idea but my solution doesn't work sometimes...'''
class Solution4:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {u: collections.deque() for u, v in tickets}
        res = ["JFK"]

        tickets.sort()
        for u, v in tickets:
            adj[u].append(v)

        def dfs(cur):
            if len(res) == len(tickets) + 1:
                return True
            if cur not in adj:
                return False

            temp = list(adj[cur])
            for v in temp:
                adj[cur].popleft()
                res.append(v)
                if dfs(v):
                    return res
                res.pop()
                adj[cur].append(v)
            return False

        dfs("JFK")
        return res

'''There's another solution to this problem that finds paths and when it gets stuck just marks that as
the end, retreats back to the previous edge and performs dfs again until it gets stuck and makes that 
the end, etc.'''



if __name__ == "__main__":
    sol = Solution() 
    
    print(sol.findItinerary([["EZE","AXA"],["TIA","ANU"],["ANU","JFK"],["JFK","ANU"],["ANU","EZE"],["TIA","ANU"],["AXA","TIA"],["TIA","JFK"],["ANU","TIA"],["JFK","TIA"]]))