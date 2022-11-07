class Solution:
    def maximum69Number (self, num: int) -> int:
        digits = list(str(num))
        
        try:
            i = digits.index('6')
            digits[i] = '9'
        except:
            pass
        
        return int("".join(digits))
        
        