# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root == None:
            return None
        if root.right == None and root.left == None:
            return root
        if root.right != None:
            root.right = self.invertTree(root.right)
        if root.left != None:
            root.left = self.invertTree(root.left)
        root = invert(root)
        return root
        
        
        
def invert(node):
    tmp = node.right
    node.right = node.left
    node.left = tmp
    return node
