class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def contains(node, target):
            if not node:
                return False
            if node == target:
                return True
            return contains(node.left, target) or contains(node.right, target)

        if ((root == p and contains(root, q)) or (root == q and contains(root, p))
            or (contains(root.left, p) and contains(root.right, q))
            or (contains(root.right, p) and contains(root.left, q))):
            return root

        if contains(root.left, p) and contains(root.left, q):
            return self.lowestCommonAncestor(root.left, p, q)

        if contains(root.right, p) and contains(root.right, q):
            return self.lowestCommonAncestor(root.right, p, q)