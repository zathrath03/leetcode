class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        
        adjacency_list = defaultdict(set)
        
        for edge in edges:
            adjacency_list[edge[0]].add(edge[1])
            adjacency_list[edge[1]].add(edge[0])
        
        def dfs(node, parent):
            if node not in adjacency_list: return 0
            
            total_time = 0
            for child in adjacency_list[node]:
                if child == parent: continue
                child_time = dfs(child, node)
                if child_time > 0 or hasApple[child]:
                    total_time += child_time + 2
            return total_time
        
        return dfs(0, -1)
