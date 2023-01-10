# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack_p = []
        stack_q = []
        
        stack_p.append(p)
        stack_q.append(q)
        
        while stack_p and stack_q:
            node_p, node_q = stack_p.pop(), stack_q.pop()
            if not node_p and not node_q: continue
            if not node_p or not node_q or node_p.val != node_q.val:
                return False
            stack_p.append(node_p.right)
            stack_p.append(node_p.left)
            stack_q.append(node_q.right)
            stack_q.append(node_q.left)
            
        if stack_p or stack_q:
            return False
        
        return True
