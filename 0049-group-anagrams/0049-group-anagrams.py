class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = defaultdict(list)

        for chars in strs:
            counts = tuple(sorted(Counter(chars).items()))
            anagrams[counts].append(chars)

        return list(anagrams.values())