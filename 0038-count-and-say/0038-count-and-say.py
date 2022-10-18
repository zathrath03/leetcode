class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        string = self.countAndSay(n-1)
        
        curr_digit = string[0]
        count = 0
        output = ""
        
        for digit in string:
            if digit == curr_digit:
                count += 1
            else:
                output += str(count) + curr_digit
                curr_digit = digit
                count = 1
        output += str(count) + curr_digit
                
        return output