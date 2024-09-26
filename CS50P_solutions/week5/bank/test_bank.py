from bank import value

def test_hello():
    assert value("hello") == 0
    assert value("Hello") == 0

def test_hxx():
    assert value("hi") == 20
    assert value("Hi") == 20

def test_random():
    assert value("What's up?") == 100
    assert value("what's up?") == 100
