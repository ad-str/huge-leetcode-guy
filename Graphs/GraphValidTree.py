from typing import List 

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        par = [i for i in range(n)]
        rank = [1 for i in range(n)]

        def find(a):
            cur = a 

            while cur != par[cur]:
                par[cur] = par[par[cur]]
                cur = par[cur]
            return cur 
        
        def union(a,b):
            parA, parB = find(a), find(b)

            if parA == parB:
                return False
            
            if rank[parA] < rank[parB]:
                par[a] = parB 
                rank[parB] += rank[parA]
            else:
                par[b] = parA 
                rank[parA] += rank[parB]
            return True
        
        for a, b in edges:
            if not union(a,b):
                return False 
            
        return True
