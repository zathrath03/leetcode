class Solution:
    def numberOfGoodPaths(self, vals, edges):
        edges.sort(key=lambda x: max(vals[x[0]], vals[x[1]]))

        goodPaths = n = len(vals)
        par = [i for i in range(n)]
        rank = [1]*n

        def find(p):
            while par[p] != p:
                par[p]= par[par[p]]
                p = par[p]
            return p

        for a,b in edges:
            parent_a, parent_b = find(a), find(b)

            if vals[parent_a] == vals[parent_b]:
                goodPaths += rank[parent_a] * rank[parent_b]
                par[parent_a] = parent_b
                rank[parent_b] += rank[parent_a]
            elif vals[parent_a] > vals[parent_b]:
                par[parent_b] = parent_a
            else:
                par[parent_a] = parent_b

        return goodPaths
