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
        
        levelOrder = []
        
        def levelOrderRecursive(node, level):
            if len(levelOrder) == level:
                levelOrder.append([])
            levelOrder[level].append(node.val)
            if node.left:
                levelOrderRecursive(node.left, level+1)
            if node.right:
                levelOrderRecursive(node.right, level+1)
        
        levelOrderRecursive(root, 0)
        return levelOrder
