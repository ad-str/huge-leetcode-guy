# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''My first attempt and it worked! Uses regular BFS using a stack but the stack also keeps track of
    level for each node. Try doing this with a dequeue.'''
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