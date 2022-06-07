# LIBS
from lambda_function import lambda_handler

# INPUTS
EVENT_VALID = {
    'numbers': [1, 2.5, 3, 10]
}
RESPONSE_VALID = {
    'statusCode': 200,
    'body': '16.5'
}

EVENT_INVALID = {
    'numbers': "Not a list"
}
RESPONSE_INVALID = {
    'statusCode': 400,
    'body': 'Invalid list of numbers'
}

# TESTS
def test_lambda_handler_valid():
    """
    Tests if lambda_handler() returns the expected result for a valid event.
    """

    assert lambda_handler(EVENT_VALID, None) == RESPONSE_VALID

def test_lambda_handler_invalid():
    """
    Tests if lambda_handler() returns the expected result for an invalid event.
    """

    assert lambda_handler(EVENT_INVALID, None) == RESPONSE_INVALID
