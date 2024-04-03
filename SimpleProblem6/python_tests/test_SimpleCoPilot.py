import pytest
import sys
sys.path.append('.')
from SimpleCoPilot import find_largest_integer

def test_find_largest_integer():
    # Test case with a single list
    assert find_largest_integer([[1, 2, 3]]) == 3

    # Test case with multiple lists
    assert find_largest_integer([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 9

    # Test case with negative numbers
    assert find_largest_integer([[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]) == -1

    # Test case with an empty list
    assert find_largest_integer([]) == float('-inf')

    # Test case with an empty sublist
    assert find_largest_integer([[], [1, 2, 3]]) == 3

    # Test case with a mix of positive and negative numbers
    assert find_largest_integer([[1, -2, 3], [-4, 5, -6], [7, -8, 9]]) == 9

    # Test case with duplicate numbers
    assert find_largest_integer([[1, 2, 3], [3, 2, 1]]) == 3

    # Test case with a single number
    assert find_largest_integer([[42]]) == 42

    # Test case with large numbers
    assert find_largest_integer([[1000000, 2000000, 3000000], [4000000, 5000000, 6000000]]) == 6000000

    # Test case with a mix of integers and non-integers
    with pytest.raises(TypeError):
        find_largest_integer([[1, 2, 3], [4, 5, '6'], [7, 8, 9]])
