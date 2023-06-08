# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''My first attempt and solution. Pretty simple bfs algorithm. The solution is basically the
    right-most node for each level of the tree.'''
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = collections.deque() 
        if root:
            q.append(root)

        while q:
            width = len(q)

            for i in range(width):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

                # append to result if we are at the right-most node of the level
                if i == width - 1:
                    res.append(node.val)
        
        return res
    

class Solution2:
    '''This solution doesn't care if root is null or not. It keeps track of the right node for each
    iteration of the level.'''
    def rightSideView(self, root: TreeNode) -> List[int]:
        res = []
        q = collections.deque([root])

        while q:
            rightSide = None
            qLen = len(q)

            for i in range(qLen):
                node = q.popleft()
                if node:
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)
            if rightSide:
                res.append(rightSide.val)
        return res
