
'''My thought process was to find the cheapest path and determine if that path contained less than or
equal to K nodes. However, the error in my ways was the fact that even if the shortest path was longer
than K, that does not mean there is NO path from src to dst. So in order to use Dijkstra's, we must 
modify it to consider ALL paths, not just the optimal ones. Hence the run time is way too much:
O(n^k * k * logn) assuming we use a heap for path costs.'''
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # make adjacency list
        adj = defaultdict(list)
        par = {}
        for x, y, p in flights:
            adj[x].append([p, y])
            par[y] = y
        

        heap = [[0, src]]
        visit = {src}

        minC = 0
        while heap:
            c, v = heapq.heappop(heap)
            

            if v == dst:
                minC = c
            
            for neiC, nei in adj[v]:
                if nei not in visit:
                    heap.heappush([neiC + c, nei])
                    par[nei] = v
                    
        if len(par) <= k:
            return minC
        else:
            return -1
        
'''My next attempt was closely related to my first and was before I realized that Dijkstra's was too slow.'''
class Solution2:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # make adjacency list
        adj = defaultdict(list)
        for x, y, p in flights:
            adj[x].append([p, y])
        

        heap = [[0, src, -1]]

        while heap:
            c, v, l = heapq.heappop(heap)

            if l > k:
                continue
            
            if v == dst:
                return c
            
            for neiC, nei in adj[v]:
                heapq.heappush(heap, [neiC + c, nei, l + 1])
                    
                    
        return -1

'''Once I realized Dijkstra's was too slow, I used Bellman-Ford.'''
class Solution3:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # let's try a Bellman-Ford Algorithm

        # make adjacency list
        adj = defaultdict(list)
        for x, y, p in flights:
            adj[x].append((y, p))
        
        # matrix for distances where each row represents how many nodes are allowed
        dist = [[float("inf") for _ in range(n)] for _ in range(k+1)]

        # initialize first row
        dist[0][src] = 0
        for nei, p in adj[src]:
            dist[0][nei] = p
        
        for i in range(k):
            for s in range(n):
                if dist[i][s] < dist[i+1][s]:
                    dist[i+1][s] = dist[i][s]
                # could get better by using path to a neighbor and taking the edge to j
                for d, c in adj[s]:
                    if dist[i][s] + c < dist[i+1][d]:
                        dist[i+1][d] = dist[i][s] + c
        
        return -1 if dist[k][dst] == float("inf") else dist[k][dst]

'''A more condensed implementation of Bellman-Ford. Instead of using an adjacency list, we just iterate
over all edges directly. And instead of a optimal cost matrix, it uses a cost array and a temp array at
each iteration. Theoretically same running time.'''
class Solution4:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # array of costs to reach node
        cost = [float("inf")] * n

        # initialize cost for source
        cost[src] = 0
        
        # iterate k times to represent allowing for more nodes in path
        for i in range(k+1):
            temp = cost[:]

            for s, d, p in flights:
                if cost[s] + p < temp[d]:
                    temp[d] = cost[s] + p
            
            cost = temp
        
        return -1 if cost[dst] == float("inf") else cost[dst]
                