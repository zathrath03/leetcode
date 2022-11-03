class Solution:
    def longestPalindrome(self, words: list[str]) -> int:
        self.init()

        for word in words:
            self.determine_if_needed(word)
        self.increment_output_if_single_double_letter_word()
        return self.output

    def increment_output_if_single_double_letter_word(self):
        if self.double_letter_words:
            self.output += 2

    def determine_if_needed(self, word):
        if word in self.needed_words:
            self.handle_needed_words(word)
        else:
            self.handle_new_words(word)

    def init(self):
        self.needed_words: defaultdict[str, int] = defaultdict(int)
        self.output = 0
        self.double_letter_words = 0

    def handle_new_words(self, word):
        self.increment_double_letters(word)
        self.needed_words[word[::-1]] += 1

    def increment_double_letters(self, word):
        if word[0] == word[1]:
            self.double_letter_words += 1

    def handle_needed_words(self, word):
        self.decrement_double_letters(word)
        self.decrement_candidates(word)
        self.output += 4

    def decrement_candidates(self, word):
        self.needed_words[word] -= 1
        if self.needed_words[word] == 0:
            del self.needed_words[word]

    def decrement_double_letters(self, word):
        if word[0] == word[1]:
            self.double_letter_words -= 1
