class Solution:
    
    def palindromePairs(self, words: list[str]) -> list[list[int]]:
        word_lookup = {w: i for i, w in enumerate(words)}
        output = []
        
        def allValidWord1s(word: str) -> set:
            valid_word1s = set()
            for i in range(len(word)):
                slc = word[:i+1]
                rev = slc[::-1]
                if slc == rev:
                    valid_word1s.add(word[i+1:][::-1])
            return valid_word1s
        
        
        def allValidWord2s(word: str) -> set:
            valid_word2s = set()
            for i in range(len(word)-1, -1, -1):
                slc = word[i:]
                rev = slc[::-1]
                if slc == rev:
                    valid_word2s.add(word[:i][::-1])
            return valid_word2s
        

        def getIndexes(words: set) -> set:
            indexes = set()
            for word in words:
                index = word_lookup.get(word)
                if index is not None:
                    indexes.add(index)
            return indexes
        
        
        for i, w in enumerate(words):
            rev_index = word_lookup.get(w[::-1])
            if rev_index is not None and rev_index != i:
                output.append([i, rev_index])
            for index in getIndexes(allValidWord1s(w)):
                output.append([index, i])
            for index in getIndexes(allValidWord2s(w)):
                output.append([i, index])

        return output