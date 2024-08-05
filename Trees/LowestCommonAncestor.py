# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    '''My original solution I did not connect the dots to use the fact it was a BST and not just a BT.
    This solution just assumes it is a BT but it works.'''
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # some edge cases for p and q - don't have to handle case where both are null since we know they are not equal
        if p and not q:
            return p
        elif not p and q:
            return q
        
        # initialize common ancestor
        res = None

        def dfs(node, p, q):
            nonlocal res

            if self.isAncestor(node, p) and self.isAncestor(node, q):
                res = node

                # check if there is a lower ancestor in left or right subtree
                dfs(node.left, p, q)
                dfs(node.right, p, q)
            
            # stop when node is no longer an ancestor of both
            return
        
        dfs(root, p, q)
        return res


    def isAncestor(self, node: 'TreeNode', other: 'TreeNode') -> bool:
        if not other:
            return True
        if not node:
            return False
        if node == other:
            return True
        
        return self.isAncestor(node.left, other) or self.isAncestor(node.right, other)
    


class Solution2:
    '''After watching the solution, I realized that I didn't realize it was a BST so I went back and 
    attempted the problem again. This hinges on the fact that the solution is basically where the node
    splits to each p and q.'''
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # some edge cases for p and q - don't have to handle case where both are null since we know they are not equal
        if p and not q:
            return p
        elif not p and q:
            return q
        
        if p.val > q.val:
            tmp = p
            p = q
            q = tmp

        if p.val <= root.val <= q.val:
            return root
        
        if root.val < p.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return self.lowestCommonAncestor(root.left, p, q)

# 2024-08-04
class Solution3:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val:
            b = p
            s = q
        else:
            b = q
            s = p 

        def dfs(node):
            if s.val <= node.val <= b.val:
                return node
            elif b.val < node.val:
                return dfs(node.left)
            elif node.val < s.val:
                return dfs(node.right)
        
        return dfs(root)
    
    def optimal(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while True:
            if root.val < p.val and root.val < q.val:
                root = root.right
            elif root.val > p.val and root.val > q.val:
                root = root.left
            else:
                return root
