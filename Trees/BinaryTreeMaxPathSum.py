# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''My first attempt and it worked! Also got it done in about 50 min. Pretty proud of this one.'''
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = -float("infinity")

        # this function returns the maximum sum of all paths that start/end at the root
        def dfs(node):
            nonlocal res

            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            # get max path to root
            maxPathToRoot = node.val + max(left, right)

            # get sum of path from left subtree to right subtree, passing through root
            pathThruBothSubtrees = left + right + node.val

            # update res if applicable
            res = max(res, node.val, maxPathToRoot, pathThruBothSubtrees)

            # return the maxPathSum that passes through the root
            return max(node.val, maxPathToRoot)
        
        dfs(root)
        return res