class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        charMap = {}
        for i, char in enumerate(s):
            if charMap.setdefault(char, t[i]) != t[i]:
                return False
            if len([key for key, value in charMap.items() if value == t[i]]) > 1:
                return False
        return True