import pytest
from fparser import example_add_func

def test_example():
    assert example_add_func(3, 4) == 8, 'example_add_func is not adding properly.' 

@pytest.mark.parametrize('x,y,result', [
    (3, 4, 7),
    (3, 4, 8)
    ])
def test_example2(x, y, result):
    assert example_add_func(x, y) == result, 'example_add_func is not adding properly.'