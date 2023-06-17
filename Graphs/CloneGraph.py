"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    '''I couldn't get this on my first try. Now that I know what dfs for graphs looks like, hopefully 
    I do better going forward.'''
    def cloneGraph(self, node: 'Node') -> 'Node':
        visit = {}

        def clone(node):
            if node in visit:
                return visit[node]
            
            copy = Node(node.val)
            visit[node] = copy
            for nb in node.neighbors:
                copy.neighbors.append(clone(nb))
            return copy
        
        return clone(node) if node else None