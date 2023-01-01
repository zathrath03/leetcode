internal static class Extensions {
    public static IEnumerable<(int, T)> Enumerate<T>(this IEnumerable<T> input, int start = 0)
    {
        var i = start;
        foreach (var t in input) yield return (i++, t);
    }
}

public class Solution {
    public bool WordPattern(string pattern, string s)
    {
        var tokens = s.Split(' ');
        if (pattern.Length != tokens.Length || pattern.Distinct().Count() != tokens.Distinct().Count())
            return false;

        var patternMap = new Dictionary<char, string>();
        foreach (var (i, c) in pattern.Enumerate())
        {
            var token = tokens[i];
            if (patternMap.TryGetValue(c, out var storedToken))
            {
                if (token != storedToken) return false;
            }
            else
            {
                patternMap.Add(c, token);
            }
        }

        return true;
    }
}