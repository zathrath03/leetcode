"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:   
    def preorder(self, root: 'Node') -> List[int]:                
        if not root:
            return []
        
        preorder = []        
        stack = [root]
                    
        while stack:
            root = stack.pop()
            preorder.append(root.val)
            for i in range(len(root.children)-1, -1, -1):
                stack.append(root.children[i])            
        
        return preorder