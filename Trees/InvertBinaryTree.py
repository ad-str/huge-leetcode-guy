# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''I ended up having to go with an iterative version because I couldn't quite wrap my head 
        around the recursive solution even though I attempted it.'''
        # iterative version
        stack = []
        if root: stack.append(root)
        while stack:
            node = stack.pop()
            left = node.left
            right = node.right
            if left == None and right == None:
                continue
            else:
                node.left = right
                node.right = left
                if node.left: stack.append(node.left)
                if node.right: stack.append(node.right)
        
        return root


        # recursive version
        '''
        if root:
            self.recurseInverse(root)
        return root
        '''
    
    def recurseInverse(self, node: Optional[TreeNode]) -> None:
        '''So I should have just handled a null node instead of doing node.left and node.right since
        I was running into errors'''
        if node.left == None and node.right == None:
            return
        else:
            tmp = node.left
            node.left = node.right
            node.left = tmp
            if node.left: 
                self.recurseInverse(node.left)
            if node.right: 
                self.recurseInverse(node.right)

    def invertTree2(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return None 
        
        #swap left and right
        tmp = root.left
        root.left = root.right
        root.right = tmp

        # recurse on left and right children
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root