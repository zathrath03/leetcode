class Solution:
    def makeGood(self, s: str) -> str:
        
        while True:
            for i in range(len(s) - 1):
                char = s[i]
                char_val = ord(char)
                next_char_val = ord(s[i+1])
                if abs(char_val - next_char_val) == 32:
                    s = s[:i] + s[i+2:]
                    break
            else:
                break
        
        return s