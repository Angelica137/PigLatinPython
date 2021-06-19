class PigLatinTranslator:
    def __init__(self, word):
        self.word = word

    def get_word(self):
        return self.word

    def translate(self):
        consonants = ""
        translation = ""
        for char in range(0, len(self.word)):
            if self.word[char] == "a" or self.word[char] == "e" or self.word[char] == "i" or self.word[char] == "o" or self.word[char] == "u":
                break
            elif self.word[:2] == "xr":
                return self.word + "ay"
            elif self.word[:2] == "yt":
                return self.word + "ay"
            else:
                consonants += self.word[char]

        # format translation
        translation = self.word[char:len(self.word)]
        return translation + consonants + "ay"


pig1 = PigLatinTranslator("chair")
print(pig1.translate())


pig1 = PigLatinTranslator("eye")
print(pig1.translate())
