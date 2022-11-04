class Solution:
    def reverseVowels(self, s: str) -> str:
        lft, rgt = 0, len(s) - 1
        ascii_letters = set("aeiouAEIOU")
        s = [*s]
        
        while lft < rgt:
            while lft < rgt and s[lft] not in ascii_letters:
                lft += 1
            while rgt > lft and s[rgt] not in ascii_letters:
                rgt -= 1
            s[lft], s[rgt] = s[rgt], s[lft]
            lft += 1
            rgt -= 1
        
        return "".join(s)