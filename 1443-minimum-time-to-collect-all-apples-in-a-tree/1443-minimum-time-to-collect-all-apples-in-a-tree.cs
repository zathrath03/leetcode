public class Solution
{
    public Dictionary<int, HashSet<int>> AdjacencyList = new Dictionary<int, HashSet<int>>();
    public IList<bool> HasApple;

    public int MinTime(int n, int[][] edges, IList<bool> hasApple)
    {
        this.HasApple = hasApple;

        foreach (var edge in edges)
        {
            if (!AdjacencyList.TryGetValue(edge[0], out var list))
            {
                list = new HashSet<int>();
                AdjacencyList[edge[0]] = list;
            }
            list.Add(edge[1]);

            if (!AdjacencyList.TryGetValue(edge[1], out list))
            {
                list = new HashSet<int>();
                AdjacencyList[edge[1]] = list;
            }
            list.Add(edge[0]);
        }

        return dfs(0, -1);
    }

    public int dfs(int node, int parent)
    {
        if (!AdjacencyList.ContainsKey(node)) return 0;

        var totalTime = 0;
        foreach (var child in AdjacencyList[node])
        {
            if (child == parent) continue;
            var childTime = dfs(child, node);
            if (childTime > 0 || HasApple[child])
                totalTime += childTime + 2;
        }
        return totalTime;
    }
}
