# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def get_left_height(node, level = 0):
            d = 0
            while node.left:
                node = node.left
                d += 1
            return d
        
        def exists(idx, node):
            left, right = 0, right_copy
            for _ in range(d):
                pivot = left + (right - left) // 2
                if idx <= pivot:
                    node = node.left
                    right = pivot - 1
                else:
                    node = node.right
                    left = pivot + 1
            return node
                
            
        if not root:
            return 0
        
        d = get_left_height(root)
        
        if not d:
            return 1

        left, right = 1, 2**d - 1
        right_copy = right

        
        while left <= right:
            pivot = left + (right - left) // 2
            if exists(pivot, root):
                left = pivot + 1
            else:
                right = pivot - 1
        
        return right_copy + left