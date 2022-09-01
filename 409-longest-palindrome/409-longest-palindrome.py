class Solution:
    def longestPalindrome(self, s: str) -> int:
        charFrequency = {}
        length = 0
        oddPresent = False
        
        for char in s:
            charFrequency[char] = charFrequency.get(char, 0) + 1
        
        frequencies = charFrequency.values()
        
        for frequency in frequencies:
            length += frequency // 2 * 2
            if not oddPresent and frequency % 2 == 1:
                oddPresent = True

        if oddPresent:
            length += 1
            
        return length
    