class Solution:
    def countSubTrees(self, n, edges, labels):
        def dfs(node):                                      
            cnt = Counter([labels[node]])
            for u in adj[node]:
                adj[u].discard(node)
                cnt += dfs(u)   
            ans[node] = cnt[labels[node]]
            return cnt
        
        adj = defaultdict(set)
        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)
        
        ans = [0]*n
        dfs(0)        
        
        return ans 