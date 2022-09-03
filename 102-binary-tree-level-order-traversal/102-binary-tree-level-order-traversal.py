# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        levelOrder = {}
        level = 0
        
        def levelOrderRecursive(root, level):
            levelOrder.setdefault(level, []).append(root.val) 
            if root.left:
                levelOrderRecursive(root.left, level+1)
            if root.right:
                levelOrderRecursive(root.right, level+1)
        
        levelOrderRecursive(root, level)
        return list(levelOrder.values())
