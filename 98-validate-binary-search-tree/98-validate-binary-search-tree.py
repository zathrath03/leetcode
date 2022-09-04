# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        inorder = []
        
        def getInorder(node):
            if not node:
                return []
            else:
                return getInorder(node.left) + [node.val] + getInorder(node.right)
        
        inorder.extend(getInorder(root))
        
        for i in range(1, len(inorder)):
            if inorder[i-1] >= inorder[i]:
                return False
        
        return True