class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        def are_similar(word1, word2):
            return word1 == word2 or (word1, word2) in similar or (word2, word1) in similar
        
        similar = set([(word1, word2) for (word1, word2) in similarPairs])

        for word1, word2 in zip_longest(sentence1, sentence2):
            if are_similar(word1, word2): continue
            return False

        return True
