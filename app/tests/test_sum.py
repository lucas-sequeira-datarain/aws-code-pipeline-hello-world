# LIBS
from src.sum import sum_numbers

# INPUTS
NUMBERS_LIST_MULTIPLE = [1, 2.5, 3, 10]
EXPECTED_RESULT_MULTIPLE = 16.5
NUMBERS_LIST_SINGLE = [8]
EXPECTED_RESULT_SINGLE = 8

# TESTS
def test_sum_numbers_multiple():
    """
    Tests if sum_numbers() returns the expected result.
    """

    assert sum_numbers(NUMBERS_LIST_MULTIPLE) == EXPECTED_RESULT_MULTIPLE

def test_sum_numbers_single():
    """
    Tests if sum_numbers() returns the expected result.
    """

    assert sum_numbers(NUMBERS_LIST_SINGLE) == EXPECTED_RESULT_SINGLE
