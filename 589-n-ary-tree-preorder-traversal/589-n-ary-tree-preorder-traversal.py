class Solution:   
    def preorder(self, root: 'Node') -> List[int]: 
        if not root:
            return []

        preorder = []        
        stack = [root]

        while stack:
            root = stack.pop()
            preorder.append(root.val)
            stack.extend(root.children[::-1])           

        return preorder