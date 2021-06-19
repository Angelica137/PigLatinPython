from scripts.pigLatinTranslator import PigLatinTranslator


def test_word_starts_w_vowel_ads_ay_at_end():
    pig = PigLatinTranslator("eye")
    assert pig.translate() == "eyeay"


def test_word_starts_w_xr_returns_worday():
    pig = PigLatinTranslator("xray")
    assert pig.translate() == "xrayay"


def test_word_starts_w_yt_returns_worday():
    pig = PigLatinTranslator("yttria")
    assert pig.translate() == "yttriaay"


def test_word_starts_w_consonat_move_consonants_to_end():
    pig = PigLatinTranslator("chair")
    assert pig.translate() == "airchay"
