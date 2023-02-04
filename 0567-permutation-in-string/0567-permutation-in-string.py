class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_pattern = self.generate_pattern(s1)
        s1_length = len(s1)
        
        for i in range(1 + len(s2) - s1_length):
            if self.generate_pattern(s2[i : i + s1_length]) == s1_pattern:
                return True
        
        return False
    
        
    def generate_pattern(self, s: string) -> int:
        pattern = [0] * 26
        zero_base = ord('a')
        
        for c in s:
            pattern[ord(c) - zero_base] += 1
            
        return pattern
