from twttr import shorten
def test_twttr():
    assert shorten('twitter') == "twttr"
    assert shorten("AEIOU") == ""
    assert shorten("CS50") == "CS50"
    assert shorten("Python") == "Pythn"
    assert shorten("") == ""
    assert shorten(",.;:") == ",.;:"
