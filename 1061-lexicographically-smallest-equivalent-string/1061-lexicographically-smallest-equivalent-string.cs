    public class Solution
    {
        public string SmallestEquivalentString(string s1, string s2, string baseStr)
        {
            var charMap = new Dictionary<char, HashSet<char>>();
            var memo = new Dictionary<char, char>();

            foreach (var (c1, c2) in Enumerable.Zip(s1, s2))
            {
                AddToMap(charMap, c1, c2);
                AddToMap(charMap, c2, c1);
            }

            return string.Join("", baseStr.Select(c => BFS(memo, charMap, c)));
        }

        private static void AddToMap(IDictionary<char, HashSet<char>> charMap, char key, char val)
        {
            if (charMap.ContainsKey(key))
            {
                charMap[key].Add(val);
            }
            else
            {
                charMap[key] = new HashSet<char>() { val };
            }
        }

        private char BFS(IDictionary<char, char> memo, IReadOnlyDictionary<char, HashSet<char>> charMap, char c)
        {
            if (memo.ContainsKey(c)) return memo[c];
            if (!charMap.ContainsKey(c)) return c;

            var smallestChar = FindSmallestChar(charMap, c, out var seen);

            UpdateMemo(memo, seen, smallestChar);

            return smallestChar;
        }

        private static void UpdateMemo(IDictionary<char, char> memo, HashSet<char> seen, char smallestChar)
        {
            foreach (var cha in seen)
            {
                memo[cha] = smallestChar;
            }
        }

        private static char FindSmallestChar(IReadOnlyDictionary<char, HashSet<char>> charMap, char c, out HashSet<char> seen)
        {
            var smallestChar = c;
            seen = new HashSet<char>();
            var queue = new HashSet<char>() { c };

            smallestChar = SmallestCharLoop(charMap, seen, queue, smallestChar);

            return smallestChar;
        }

        private static char SmallestCharLoop(IReadOnlyDictionary<char, HashSet<char>> charMap, ISet<char> seen, HashSet<char> queue, char smallestChar)
        {
            while (queue.Count > 0)
            {
                var ch = Pop(queue);
                if (seen.Contains(ch)) continue;
                seen.Add(ch);
                smallestChar = smallestChar.CompareTo(ch) < 0 ? smallestChar : ch;
                queue.UnionWith(charMap[ch]);
            }

            return smallestChar;
        }

        private static char Pop(ICollection<char> queue)
        {
            var c = queue.First();
            queue.Remove(c);
            return c;
        }
    }
