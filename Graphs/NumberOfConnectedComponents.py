from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1 for i in range(n)]

        def find(a):
            cur = a

            # compress the path to root parent
            while cur != par[cur]:
                # make parent of current node equal to its grandparent
                par[cur] = par[par[cur]]
                cur = par[cur] 
            return cur 
        
        def union(a, b):
            parA = find(a)
            parB = find(b)

            if parA == parB:
                return 0 
            
            if rank[parA] < rank[parB]:
                par[a] = parB
                rank[parB] += rank[parA]
            else:
                par[b] = parA 
                rank[parA] += rank[parB]
            
            return 1
        
        res = n
        for n1, n2 in edges:
            res -= union(n1, n2)
        return res 
