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


def test_starts_w_constonant_and_qu():
    pig = PigLatinTranslator("square")
    assert pig.translate() == "aresquay"


def test_starts_w_consonants_follwed_by_y():
    pig = PigLatinTranslator("rhythm")
    assert pig.translate() == "ythmrhay"


def test_my_returns_ymay():
    pig = PigLatinTranslator("my")
    assert pig.translate() == "ymay"
