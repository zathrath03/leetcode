# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    
    def guessNumber(self, n: int) -> int:
        max_guess = n + 1
        min_guess = 0
        my_guess = (max_guess - min_guess) // 2
        RC = guess(my_guess)
        
        while RC:
            if RC == -1:
                max_guess = my_guess
                my_guess = (my_guess + min_guess) // 2
                RC = guess(my_guess)
            elif RC == 1:
                min_guess = my_guess
                my_guess = (max_guess + my_guess) // 2
                RC = guess(my_guess)
                
        return my_guess