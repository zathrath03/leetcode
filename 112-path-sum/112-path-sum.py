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
        if root.val == targetSum and not root.left and not root.right:
            return True
        
        if root.left and root.right:
            root.left.val += root.val
            root.right.val += root.val
            return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)
        elif root.left:
            root.left.val += root.val
            return self.hasPathSum(root.left, targetSum)
        elif root.right:
            root.right.val += root.val
            return self.hasPathSum(root.right, targetSum)
        else:
            return False