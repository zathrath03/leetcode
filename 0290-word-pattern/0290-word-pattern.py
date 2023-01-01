class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        tokens = s.split(" ")
        if len(pattern) != len(tokens):
            return False
        
        pattern_map = {}
        
        for i, char in enumerate(pattern):
            token = tokens[i]
            if pattern_map.setdefault(char, token) != token:
                return False
            
        if len(set(pattern_map.values())) != len(set(pattern)):
            return False
            
        return True