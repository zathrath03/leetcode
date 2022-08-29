class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        charMapStoT = {}
        charMapTtoS = {}
        for i, char in enumerate(s):
            if charMapStoT.setdefault(char, t[i]) != t[i]:
                return False
            if charMapTtoS.setdefault(t[i], char) != char:
                return False
        return True