class Solution:
    def intToRoman(self, num: int) -> str:
        romans = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50: "L", 90: "XC", 100: "C", 400: "CD", 500: "D", 900: "CM", 1000: "M"}
        if num in romans:
            return romans[num]
        
        sorted_roman_integers = sorted(romans.keys(), reverse=True)
        
        output = ""
        for i in range(len(sorted_roman_integers)):
            while num > 0:
                if sorted_roman_integers[i] > num:
                    break
                num -= sorted_roman_integers[i]
                output += romans[sorted_roman_integers[i]]
            
        return output