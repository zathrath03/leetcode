class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.istitle() or word.islower() or word.isupper()