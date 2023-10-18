''''
Problem: Given an acyclic undirected graph in adjaceny list form, return the number of subgraphs
Example: graph = 1-2-3, solution = 7 -> {}, {1}, {2}, {3}, {1-2}, {2-3}, {1-2-3}
'''

def countSubgraphs(adj: dict[int, list]) -> list:
    # Key observation: you can pick up the graph at any point and treat it as the
    # root of a tree (since acyclic).
    # One possible method is to pick an arbitrary point as the root and count the number
    # of subtrees. However, there are two main issues with this method:
    # 1. We need to loop over all possible roots? do we?
    # 2. We need to take into account cases like {1-2-3} rooted at 2 and
    # {1-2-3} rooted at 1. Need to treat them as the same.

    visited = set()
    def dfs(node):
        res = 1
        for child in adj[node]:
            if child not in visited:
                visited.add(child)
                res *= 1 + dfs(child)
        return res + 1

    visited.add(0)
    return dfs(0)

if __name__ == "__main__":
    adj = {
        0: [1],
        1: [0]
    }
    print(countSubgraphs(adj))
    
    adj = {
        0: [1],
        1: [0,2],
        2: [1]
    }
    print(countSubgraphs(adj))
    assert countSubgraphs(adj) == 7
    print("\nCorrect!\n")