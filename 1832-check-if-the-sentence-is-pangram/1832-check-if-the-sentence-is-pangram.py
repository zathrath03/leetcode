class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        letters = set()
        for char in sentence:
            letters.add(char)
            
        return len(letters) == 26