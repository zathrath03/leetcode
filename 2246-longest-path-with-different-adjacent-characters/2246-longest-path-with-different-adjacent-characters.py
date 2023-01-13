class Solution:
    def longestPath(self, parents: list[int], s: str) -> int:
        parent_children_map = defaultdict(set)
        for child in range(1, len(parents)):
            parent = parents[child]
            parent_children_map[parent].add(child)
                
        longest_path = 1
        
        def get_max_subtree_length(parent):
            nonlocal longest_path
            if parent not in parent_children_map:
                return 1
            
            longest_subtree_length = second_longest_subtree_length = 0
            
            for child in parent_children_map[parent]:
                child_length = get_max_subtree_length(child)
                if s[parent] != s[child]:
                    if child_length > longest_subtree_length:
                        second_longest_subtree_length = longest_subtree_length
                        longest_subtree_length = child_length
                    elif child_length > second_longest_subtree_length:
                        second_longest_subtree_length = child_length
                    
            longest_path = max(longest_path, 1 + longest_subtree_length + second_longest_subtree_length)
            
            return 1 + longest_subtree_length
        
        get_max_subtree_length(0)
        
        return longest_path
