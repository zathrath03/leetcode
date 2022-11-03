class Solution:
    def longestPalindrome(self, words: list[str]) -> int:
        self.init()

        for word in words:
            self.determine_if_needed(word)
        self.increment_output_if_double_letter_word_remains()
        return self.output

    def init(self) -> None:
        self.needed_words: defaultdict[str, int] = defaultdict(int)
        self.output = 0
        self.double_letter_words = 0

    def determine_if_needed(self, word: str) -> None:
        if word in self.needed_words:
            self.handle_needed_words(word)
        else:
            self.handle_new_words(word)

    def increment_output_if_double_letter_word_remains(self) -> None:
        if self.double_letter_words:
            self.output += 2

    def handle_needed_words(self, word: str) -> None:
        self.decrement_double_letters(word)
        self.decrement_needed_words(word)
        self.output += 4

    def handle_new_words(self, word: str) -> None:
        self.increment_double_letters(word)
        self.needed_words[word[::-1]] += 1

    def decrement_double_letters(self, word: str) -> None:
        if word[0] == word[1]:
            self.double_letter_words -= 1

    def decrement_needed_words(self, word: str) -> None:
        self.needed_words[word] -= 1
        if self.needed_words[word] == 0:
            del self.needed_words[word]

    def increment_double_letters(self, word: str) -> None:
        if word[0] == word[1]:
            self.double_letter_words += 1
