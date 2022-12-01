class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        first_half_count = second_half_count = 0
        
        for i in range(len(s) // 2):
            if s[i] in vowels:
                first_half_count += 1
            if s[len(s) - 1 - i] in vowels:
                second_half_count += 1
        
        return first_half_count == second_half_count
            