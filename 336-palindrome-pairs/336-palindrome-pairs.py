class Solution:
    
    def palindromePairs(self, words: list[str]) -> list[list[int]]:
        word_lookup = {w: i for i, w in enumerate(words)}
        output = []
        
        def allValidWord1s(word: str) -> list[str]:
            valid_word1s = set()
            for i in range(len(word)):
                slc = word[:i+1]
                rev = slc[::-1]
                if slc == rev:
                    valid_word1s.add(word[i+1:][::-1])
            return valid_word1s
        
        
        def allValidWord2s(word: str) -> list[str]:
            valid_word2s = set()
            for i in range(len(word)-1, -1, -1):
                slc = word[i:]
                rev = slc[::-1]
                if slc == rev:
                    valid_word2s.add(word[:i][::-1])
            return valid_word2s
        

        for i, w in enumerate(words):
            rev = w[::-1]
            rev_index = word_lookup.get(rev)
            if rev_index is not None and rev_index != i:
                output.append([i, rev_index])
            for word1 in allValidWord1s(w):
                word1_index = word_lookup.get(word1)
                if word1_index is not None:
                    output.append([word1_index, i])
            for word2 in allValidWord2s(w):
                word2_index = word_lookup.get(word2)
                if word2_index is not None:
                    output.append([i, word2_index])

            
        return output