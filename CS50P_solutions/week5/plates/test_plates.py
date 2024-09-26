from plates import is_valid

def test_length():
    assert is_valid("s") == False
    assert is_valid("mdkasmdkas") == False

def test_first_two_digits():
    assert is_valid("12s") == False
    assert is_valid("1kas") == False

def test_middle_digits():
    assert is_valid("das12s") == False
    assert is_valid("as1kas") == False

def test_if_digits():
    assert is_valid("das12") == True
    assert is_valid("ka33") == True
    assert is_valid("ka03") == False

def test_if_punctuation():
    assert is_valid("dasb,") == False
    assert is_valid("dab!.") == False

def test_start_with_letters():
    assert is_valid("AB123") == True
    assert is_valid("A123") == False
