class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = defaultdict(list)

        for chars in strs:
            sorted_chars = "".join(sorted(chars))
            anagrams[sorted_chars].append(chars)

        return list(anagrams.values())