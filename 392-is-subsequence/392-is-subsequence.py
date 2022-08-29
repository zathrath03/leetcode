class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        t_ptr = 0
        for char in s:
            while t_ptr < len(t) and t[t_ptr] != char:
                t_ptr += 1
            t_ptr += 1
            if t_ptr > len(t):
                return False
        
        return True