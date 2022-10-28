class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = defaultdict(list)

        for chars in strs:
            anagrams[tuple(sorted(chars))].append(chars)

        return list(anagrams.values())