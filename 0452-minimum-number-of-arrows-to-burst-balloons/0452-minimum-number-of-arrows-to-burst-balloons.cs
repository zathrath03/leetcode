public class Solution {
    public int FindMinArrowShots(int[][] points) 
    {
        points = points.OrderBy(x => x[1]).ToArray();

        var arrows = 1;
        var currentEnd = points[0][1];

        foreach (var point in points)
        {
            var start = point[0];
            var end = point[1];
            if (currentEnd >= start) continue;
            arrows++;
            currentEnd = end;
        }

        return arrows;
    }
}