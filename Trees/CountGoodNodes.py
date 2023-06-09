# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''My iterative solution.'''
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        stack = []
        if root:
            stack.append([root, -float("infinity")])

        while stack:
            node, max = stack.pop()

            if node.val >= max:
                res += 1
                max = node.val

            if node.left:
                stack.append([node.left, max])
            if node.right:
                stack.append([node.right, max])
        
        return res
    


class Solution:
    '''My recursive solution.'''
    def goodNodes(self, root: TreeNode) -> int:
        res = 0

        def dfs(root, max):
            nonlocal res

            if not root:
                return

            if root.val >= max:
                res += 1
                max = root.val
            
            dfs(root.left, max)
            dfs(root.right, max)

        dfs(root, -float("infinity"))
        return res

            