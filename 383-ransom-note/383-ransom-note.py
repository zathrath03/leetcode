class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        
        ransomDict = {}
        magDict = {}
        for char in ransomNote:
            ransomDict[char] = ransomDict.get(char, 0) + 1
        for char in magazine:
            magDict[char] = magDict.get(char, 0) + 1
        for key in ransomDict.keys():
            if ransomDict[key] > magDict.get(key, 0):
                return False
        return True