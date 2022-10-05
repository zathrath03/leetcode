# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            new_root = TreeNode(val, root)
            return new_root

        q = deque()
        q.append((root, 1))
        
        while q:
            node, node_depth = q.pop()
            if node_depth == depth:
                break
            if node_depth == depth - 1:
                node.left = TreeNode(val, node.left)
                node.right = TreeNode(val, right=node.right)
            if node.left:
                q.appendleft((node.left, node_depth + 1))
            if node.right:
                q.appendleft((node.right, node_depth + 1))
            
        return root