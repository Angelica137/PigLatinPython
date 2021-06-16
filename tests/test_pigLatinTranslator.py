from scripts.pigLatinTranslator import PigLatinTranslator


def test_word_starts_w_vowel_ads_ay_at_end():
    pig = PigLatinTranslator("eye")
    assert pig.translate() == "eyeay"


def test_word_starts_w_xr_returns_xrayay():
    pig = PigLatinTranslator("xray")
    assert pig.translate() == "xrayay"
