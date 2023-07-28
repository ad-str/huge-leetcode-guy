from typing import List
import math
import heapq
from collections import defaultdict

'''My incorrect solution. I knew I needed to heapify based on the distance but I didn't know how to do
that while also linking points to the distances.'''
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #dists = [(i, sqrt(points[i][0]**2 + points[i][1]**2)) for i in range(len(points))]
        dists = []
        map = defaultdict(list)
        for i in range(len(points)):
            dist = sqrt(points[i][0]**2 + points[i][1]**2)
            dists.append(dist)
            map[dist].append(points[i])
        
        heapq.heapify(dists)
        res = []
        while len(dists) >= k:
            dist = heapq.heappop(dists)
            res.append(map[dist].pop())
        
        return res
    
'''Neetcode solution. Apparently heapify works by taking the first value of the items as the value to 
heapify on - I didn't know that.'''
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pts = []
        for x, y in points:
            dist = (abs(x - 0) ** 2) + (abs(y - 0) ** 2)
            pts.append([dist, x, y])

        res = []
        heapq.heapify(pts)
        for i in range(k):
            dist, x, y = heapq.heappop(pts)
            res.append([x, y])
        return res


if __name__ == "__main__":
    sol = Solution()

    print(sol.kClosest([[1,3],[-2,2]], 1))