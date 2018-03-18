from week1 import fibonacci


def test_basic():
    assert fibonacci(0) == 1
    assert fibonacci(1) == 1


def test_mid():
    assert fibonacci(2) == 2
    assert fibonacci(3) == 3


def test_invalid():
    assert fibonacci(-1) == -1
    assert fibonacci(-2) == -1


def test_huge():
    assert fibonacci(300) == 222232244629420445529739893461909967206666939096499764990979600
