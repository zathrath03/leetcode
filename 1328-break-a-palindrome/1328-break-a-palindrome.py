class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        length = len(palindrome)
        if length == 1:
            return ""
        for i in range(length // 2):
            if palindrome[i] != 'a':
                return palindrome[:i] + 'a' + palindrome[i+1:]
        # if palindrome[-1] != 'a':
        #     return palindrome[:-1] + 'a'
        # else:
        return palindrome[:-1] + 'b'