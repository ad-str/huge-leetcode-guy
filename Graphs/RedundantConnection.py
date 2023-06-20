class Solution:
    '''I understood that adding an edge to a tree creates a cycle and we just need to delete one edge
    from that cycle. My idea was to performa dfs to find the cycle and just return the last edge that
    was recursed on but I couldn't get it working.'''
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # make graph using a map
        graph = defaultdict(list)
        for start, end in edges:
            graph[start].append(end)
            graph[end].append(start)
        
        cycle = set()
        def dfs(node, prev):
            if node in cycle:
                return [node, prev]
            
            cycle.add(node)
            for nei in graph[node]:
                if nei != prev:
                    if nei in cycle:
                        return [nei, node]
                    dfs(nei, node)
            cycle.remove(node)
        
        return dfs(edges[0][0], edges[0][1])
    

class Solution:
    '''Neetcode solutions using some algorithm called unionFind.'''
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        def find(n):
            p = par[n]
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p

        # return False if already unioned
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]

                