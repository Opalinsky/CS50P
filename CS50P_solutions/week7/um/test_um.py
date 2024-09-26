from um import count

def test_correct():
    assert count("UM") == 1
    assert count("um") == 1
    assert count("Um, thanks for the album.") == 1

def test_correct_multiple():
    assert count("UM um") == 2
    assert count("um umm") == 1
    assert count("Um, thanks, um...") == 2

def test_no_correct():
    assert count("jndskadj") == 0
    assert count("jasdnkasjndjkas") == 0
    assert count("ummm?") == 0


def test_incorrect():
    assert count("yummy") == 0
    assert count("kodasum") == 0
    assert count("umiversum") == 0

