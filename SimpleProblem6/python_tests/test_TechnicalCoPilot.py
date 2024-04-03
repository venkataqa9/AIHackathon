import sys
sys.path.append('.')
from TechnicalCoPilot import find_largest_integer

class TestFindLargestInteger():
    def test_empty_lists(self):
        lst = [[]]
        assert(find_largest_integer(lst) == None)

    def test_different_data_types(self):
        lst = [[1, 2, 3], ['a', 'b', 'c'], [True, False]]
        assert(find_largest_integer(lst) == 3)

    def test_negative_numbers(self):
        lst = [[-5, -10, -3], [-2, -7, -1], [-8, -4, -6]]
        assert(find_largest_integer(lst) ==  -1)

    def test_mixed_data_types(self):
        lst = [[1, 2, 3], ['a', 'b', 'c'], [True, False], [4.5, 6.7, 2.3]]
        assert(find_largest_integer(lst) == 3)
