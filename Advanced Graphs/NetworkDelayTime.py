from typing import List

'''My original solution and it works great! Dijkstra's Algorithm'''
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # construct adjacency list
        adj = {i+1: [] for i in range(n)}
        for u, v, w in times:
            adj[u].append([v, w])
        
        # perform Dijkstra's using k as source
        D = [float("inf")] * n
        D[k-1] = 0
        S = set()

        while len(S) != n:
            # argmin
            mini, mind = -1, float("inf")
            for i in range(n):
                if i+1 in S:
                    continue
                if D[i] < mind:
                    mind = D[i]
                    mini = i
            
            # if no min was found, it means we cann't connect all points        
            if mini == -1:
                return -1
            
            S.add(mini+1)

            # relax edges
            for nei, w in adj[mini+1]:
                if D[mini] + w < D[nei-1]:
                    D[nei-1] = D[mini] + w
        
        return max(D) 


if __name__ == "__main__":
    sol = Solution() 

    print(sol.networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2))