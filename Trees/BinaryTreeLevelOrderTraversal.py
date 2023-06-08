# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''My first attempt and it worked! It works by keeping track of the level at each node. However, 
    this is actually a DFS iterative algorithm since it uses a stack instead of a queue. If we used
    a queue we wouldn't have to keep track of the level this way - see next solution.'''
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        stack = []
        stack.append((root, 0))

        while stack:
            node, level = stack.pop()

            if node.right:
                stack.append((node.right, level + 1))
            if node.left:
                stack.append((node.left, level + 1))
            
            if level >= len(res):
                res.append([node.val])
            else:
                res[level].append(node.val)
        
        return res
    

class Solution2:
    '''This is a proper BFS algorithm since it uses a queue.'''
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        q = collections.deque()
        if root:
            q.append(root)

        while q:
            val = []

            for i in range(len(q)):
                node = q.popleft()
                val.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(val)
        return res
