public class Solution {
    public int ClosestMeetingNode(int[] edges, int node1, int node2) {
        if ( node1 == node2) return node1;

        var visited1 = new HashSet<int> {node1};
        var visited2 = new HashSet<int> {node2};

        var closestNode = int.MaxValue;

        while (true) {
            if (node1 != -1)
                node1 = edges[node1];
            if (node2 != -1)
                node2 = edges[node2];

            if (visited1.Contains(node1) && visited2.Contains(node2)) break;

            visited1.Add(node1);
            visited2.Add(node2);

            if (visited2.Contains(node1))
                closestNode = node1;
            if (node2 < closestNode && visited1.Contains(node2))
                closestNode = node2;
            if (closestNode < int.MaxValue)
                return closestNode;
        }

        return -1;
    }
}
