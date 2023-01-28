public class SummaryRanges
{
    private readonly SortedSet<int> _integersSeen;

    public SummaryRanges()
    {
        _integersSeen = new SortedSet<int>();
    }

    public void AddNum(int value)
    {
        _integersSeen.Add(value);
    }

    public int[][] GetIntervals()
    {
        if (_integersSeen.Count == 0) return Array.Empty<int[]>();

        var intervals = new List<int[]>();
        var (left, right) = (-1, -1);

        foreach (var num in _integersSeen)
        {
            if (left < 0)
            {
                left = right = num;
            } else if (num == right + 1)
            {
                right = num;
            }
            else
            {
                intervals.Add(new int[] {left, right});
                left = right = num;
            }
        }
        intervals.Add(new int[] {left, right});
        return intervals.ToArray();
    }
}

/**
 * Your SummaryRanges object will be instantiated and called as such:
 * SummaryRanges obj = new SummaryRanges();
 * obj.AddNum(value);
 * int[][] param_2 = obj.GetIntervals();
 */