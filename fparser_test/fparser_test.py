import pytest
import fparser

def test_example():
    """
    Test to determine if function example_add_func is working properly.
    """
    assert fparser.example_add_func(3, 4) == 7, 'example_add_func is not adding properly.' 

@pytest.mark.parametrize('x,y,result', [
    (3, 4, 7),
    (4, 4, 8)
    ])
def test_example2(x, y, result):
    """
    Multiple tests to determine if function example_add_func is working properly.

    Args:
        x (float): 
        y (float):
        result (float):
    """
    assert fparser.example_add_func(x, y) == result, 'example_add_func is not adding properly.'