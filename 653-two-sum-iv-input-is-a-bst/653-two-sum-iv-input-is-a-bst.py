# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        needed = set()
        stack = deque()
        stack.append(root)
        
        while stack:
            node = stack.pop()
            need = k - node.val
            
            if node.val in needed:
                return True
            else:
                needed.add(k - node.val)
            
            if node.left:  # and need < node.val:
                stack.append(node.left)
            if node.right:  # and need > node.val:
                stack.append(node.right)
            
        return False