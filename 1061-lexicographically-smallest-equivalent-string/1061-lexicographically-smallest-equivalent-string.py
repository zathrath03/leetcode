class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        char_map = defaultdict(set)

        for c1, c2 in zip(s1, s2):
            char_map[c1].add(c2)
            char_map[c2].add(c1)

        memo = {}        
        def bfs(char: str) -> str:
            if char in memo:
                return memo[char]

            if char not in char_map:
                return char

            smallest_char = char
            seen = set()
            queue = {char}

            while queue:
                char = queue.pop()
                if char in seen: continue
                seen.add(char)
                smallest_char = min(char, smallest_char)
                queue |= char_map[char]

            for char in seen:
                memo[char] = smallest_char

            return smallest_char

        return "".join(bfs(char) for char in baseStr)
