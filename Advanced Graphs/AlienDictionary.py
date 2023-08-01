'''My solution. Took me a little while but I eventually realized it is a topological sort problem. Had
to be a little creative in how I made the adjacency list. Once I made the graph, it's just a matter of
topologically sorting.'''
from typing import (
    List,
)

class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """
    def alien_order(self, words: List[str]) -> str:
        # Write your code here

        # create an adjacency list 
        adj = defaultdict(set)

        # iterate over words, looking at two words at a time
        for i in range(len(words)-1):
            left = words[i]
            right = words[i+1]

            # iterate over characters, first instance of a different char means
            # a directed edge in the adj list 
            for ci in range(len(left)):
                if left[ci] != right[ci]:
                    adj[left[ci]].add(right[ci])
                    break
        
        # now do a topological sort 
        visit = set()
        res = []
        def dfs(c):
            visit.add(c)
            for nei in adj[c]:
                if nei not in visit:
                    dfs(nei)
            res.append(c)
        
        for c, neis in adj:
            if c in visit:
                continue
            dfs(c)
            
        return "".join(res[::-1])