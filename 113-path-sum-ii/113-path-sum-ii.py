# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        if not root: return []
        stack = []
        output = []
        stack.append([root, 0])
        
        
        while stack:
            path = stack.pop()
            cur_sum = path.pop()
            node = path.pop()
            if node.left:
                left_path = path.copy()
                left_path.extend([node.val, node.left, cur_sum + node.val])
                stack.append(left_path)
            if node.right:
                right_path = path.copy()
                right_path.extend([node.val, node.right, cur_sum + node.val])
                stack.append(right_path)
            if not node.left and not node.right:
                if cur_sum + node.val == targetSum:
                    path.append(node.val)
                    output.append(path)
                    
        return output