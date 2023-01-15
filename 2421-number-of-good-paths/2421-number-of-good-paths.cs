public class Solution
{
    public int NumberOfGoodPaths(int[] vals, int[][] edges)
    {
        var sortedEdges = edges.OrderBy(x => Math.Max(vals[x[0]], vals[x[1]]));
        var n = vals.Length;
        var goodPaths = n;
        var par = Enumerable.Range(0, n).ToArray();
        var rank = Enumerable.Repeat(1, n).ToArray();

        foreach (var edge in sortedEdges)
        {
            var parentA = FindParent(edge[0], par);
            var parentB = FindParent(edge[1], par);

            if (vals[parentA] == vals[parentB])
            {
                goodPaths += rank[parentA] * rank[parentB];
                par[parentA] = parentB;
                rank[parentB] += rank[parentA];
            }
            else if (vals[parentA] > vals[parentB])
            {
                par[parentB] = parentA;
            }
            else
            {
                par[parentA] = parentB;
            }
        }

        return goodPaths;
    }

    private static int FindParent(int p, IList<int> par)
    {
        while (par[p] != p)
        {
            par[p] = par[par[p]];
            p = par[p];
        }

        return p;
    }
}