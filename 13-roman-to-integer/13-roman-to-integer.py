class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int_map = { "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        integer = 0
        i = 0
        while i < len(s):
            if i == len(s)-1:
                integer += roman_to_int_map[s[i]]
            elif roman_to_int_map[s[i]] < roman_to_int_map[s[i+1]]:
                integer += roman_to_int_map[s[i+1]] - roman_to_int_map[s[i]]
                i += 1
            else:
                integer += roman_to_int_map[s[i]]
            i += 1
        return integer