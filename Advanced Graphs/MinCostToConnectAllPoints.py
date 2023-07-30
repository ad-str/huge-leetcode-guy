from typing import List

'''My original solution. It took a minute to figure out a bug with the construction of the adjacency 
matrix. In the first line I originally did [[0] * len(points)] * len(points), but apparently the inner
lists are all referring to the same object that way, so all rows change in tandem. List comprehension
avoids this. Anyway, the problem reduces to finding the MST of a maximally connected graph. Since it's
maximally connected meaning |E| = O(|V|^2), I chose to use an Adjacency Matrix and Prim's algorithm 
which are both O(n^2).'''
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # construct the adjacency matrix
        G = [[0 for _ in range(len(points))] for _ in range(len(points))]
        for i in range(len(points)):
            for j in range(len(points)):
                G[i][j] = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
        
        W = [0] * len(points)
        cost = 0
        V = set()

        # choose a vertex to start with
        V.add(0)
        W[0] = float("inf")
        for j in range(1, len(points)):
            W[j] = G[0][j]
        
        # Prim's
        while len(V) != len(points):
            # find argmin 
            mini, minc = 0, float("inf")
            for i, v in enumerate(W):
                if v < minc:
                    mini = i
                    minc = v

            cost += minc
            V.add(mini)
            W[mini] = float("inf")

            # relax edge weights        
            for i, v in enumerate(G[mini]):
                if i in V:
                    continue
                
                if v < W[i]:
                    W[i] = v

        return cost




if __name__ == "__main__":
    sol = Solution()

    print(sol.minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]]))