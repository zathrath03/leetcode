# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        
        def contains(node, target):
            if not node:
                return False
            if node == target:
                return True
            return contains(node.left, target) or contains(node.right, target)
        
        
        # node is p or q and other is a child of node
        # left contains p and right contains q
        # right contains p and left contains q
        if ((root == p and contains(root, q)) or (root == q and contains(root, p))
            or (contains(root.left, p) and contains(root.right, q))
            or (contains(root.right, p) and contains(root.left, q))):
            
            return root

        # left contains both p and q
        if contains(root.left, p) and contains(root.left, q):
            return self.lowestCommonAncestor(root.left, p, q)

        # right contains both p and q
        if contains(root.right, p) and contains(root.right, q):
            return self.lowestCommonAncestor(root.right, p, q)

        # return root