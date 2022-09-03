class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = collections.deque()
        levelOrder = []
        queue.append((root, 0))
        
        while queue:
            node, level = queue.popleft()
            if len(levelOrder) == level:
                levelOrder.append([])
            levelOrder[level].append(node.val)
            if node.left:
                queue.append((node.left, level+1))
            if node.right:
                queue.append((node.right, level+1))

        return levelOrder