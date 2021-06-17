import pytest

def function(a, b):
        return a/b


def test_function():
    assert function(6, 3) == 2


# def test_function1():
#     assert function(6, 5) == 2


class customexception(TypeError):
    pass


def test_reqstr2obj():
    with pytest.raises(customexception):
        function(2, 0)