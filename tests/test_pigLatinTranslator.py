from scripts.pigLatinTranslator import PigLatinTranslator


def test_word_starts_w_vowel_ads_ay_at_end():
    pig = PigLatinTranslator("eye")
    assert pig.translate() == "eyeay"
