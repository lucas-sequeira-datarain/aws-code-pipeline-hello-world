# LIBS
from src.validator import validate_list_of_numbers

# INPUTS
VALID_NUMBERS_LIST = [1, 2.5, 3, 10]
INVALID_NUMBERS_LIST = [1, '2.5', 3, 10]
INVALID_NUMBERS_EMPTY_LIST = []
INVALID_NUMBERS_NON_LIST = '1, 2.5, 3, 10'
INVALID_NUMBERS_NON_LIST_NONE = None

# TESTS
def test_validate_list_of_numbers_valid_list():
    """
    Tests if validate_list_of_numbers() returns True for a valid list of numbers.
    """

    assert validate_list_of_numbers(VALID_NUMBERS_LIST) == True

def test_validate_list_of_numbers_invalid_list():
    """
    Tests if validate_list_of_numbers() returns False for an invalid list of numbers.
    """

    assert validate_list_of_numbers(INVALID_NUMBERS_LIST) == False

def test_validate_list_of_numbers_invalid_empty_list():
    """
    Tests if validate_list_of_numbers() returns False for an invalid empty list of numbers.
    """

    assert validate_list_of_numbers(INVALID_NUMBERS_EMPTY_LIST) == False

def test_validate_list_of_numbers_invalid_non_list():
    """
    Tests if validate_list_of_numbers() returns False for an invalid non-list of numbers.
    """

    assert validate_list_of_numbers(INVALID_NUMBERS_NON_LIST) == False

def test_validate_list_of_numbers_invalid_non_list_none():
    """
    Tests if validate_list_of_numbers() returns False for an invalid non-list of numbers.
    """

    assert validate_list_of_numbers(INVALID_NUMBERS_NON_LIST_NONE) == False
