import pytest
from fuel import convert, gauge

def test_gauge():
    assert gauge(99) == 'F'
    assert gauge(75) == "75%"
    assert gauge(1) == 'E'

def test_convert():
    # Testy dla prawidłowych ułamków
    assert convert("3/4") == 75
    assert convert("1/1") == 100
    assert convert("0/1") == 0
    assert convert("1/2") == 50

    # Testowanie błędów przy użyciu składni with...raises
    with pytest.raises(ValueError):
        convert("3/2")  # X > Y

    with pytest.raises(ZeroDivisionError):
        convert("1/0")  # dzielenie przez 0

    with pytest.raises(ValueError):
        convert("a/b")  # nieprawidłowe wartości

    with pytest.raises(ValueError):
        convert("3/")  # brak Y

    with pytest.raises(ValueError):
        convert("/4")  # brak X
