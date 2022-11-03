class Solution:
    def longestPalindrome(self, words: list[str]) -> int:
        candidates = defaultdict(int)
        output = 0
        double_letter_words = 0

        for word in words:
            if word in candidates:
                if word[0] == word[1]:
                    double_letter_words -= 1
                candidates[word] -= 1
                if candidates[word] == 0:
                    del candidates[word]
                output += 4
            else:
                if word[0] == word[1]:
                    double_letter_words += 1
                candidates[word[::-1]] += 1
        if double_letter_words:
            output += 2
        return output