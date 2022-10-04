# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return root.val == targetSum
        
        sums = set()
        def travel(node, parentSum):
            parentSum = parentSum + node.val
            if node.left:
                travel(node.left, parentSum)
            if node.right:
                travel(node.right, parentSum)
            if not node.left and not node.right:
                sums.add(parentSum)
        
        travel(root, 0)
        return targetSum in sums