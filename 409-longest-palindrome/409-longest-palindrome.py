class Solution:
    def longestPalindrome(self, s: str) -> int:
        length = 0
        oddPresent = False
        
        for frequency in collections.Counter(s).values():
            length += frequency // 2 * 2
            if not oddPresent and frequency % 2 == 1:
                oddPresent = True

        if oddPresent:
            length += 1
            
        return length    