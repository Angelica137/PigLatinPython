class PigLatinTranslator:
    def __init__(self, word):
        self.word = word

    def get_word(self):
        return self.word

    def translate(self):
        if self.word[0] == "a" or self.word[0] == "e" or self.word[0] == "i" or self.word[0] == "o" or self.word[0] == "u":
            return self.word + "ay"
