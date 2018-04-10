from roman_exercise import from_roman
from roman_exercise import to_roman


def test_to_roman_basic_i():
    assert 'I' == to_roman(1)


def test_from_roman_basic_1():
    assert 1 == from_roman("I")
