# iterative dfs

class TreeNode:
    
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def idfs(node, val):
    stack = []
    cur = node

    while stack or cur:
        if not cur:
            cur = stack.pop()

        print(cur.val)

        if cur.val == val:
            return True

        if cur.right:
            stack.append(cur.right)
        cur = cur.left
    
    return False


def rdfs(node, val):
    if not node:
        return False
    
    if node.val == val:
        return True
    
    print(node.val)
    return rdfs(node.left, val) or rdfs(node.right, val)

if __name__ == "__main__":
    root = TreeNode(6)
    root.right = TreeNode(10)
    root.left = TreeNode(2)
    root.right.right = TreeNode(11)
    root.right.left = TreeNode(8)
    root.left.right = TreeNode(4)

    #print(idfs(root, 11))
    print(rdfs(root, 12))