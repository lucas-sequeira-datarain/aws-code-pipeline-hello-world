# METHODS

def validate_list_of_numbers(numbers: list) -> bool:
    """
    Validates that a list of numbers is a list of numbers.
    
    Params:
    -------
        numbers (list): list of numbers
    
    Returns:
    --------
        bool: True if numbers is a list of integers or float, False otherwise
    """
    # Initialize valid
    valid = True

    # Check if numbers is a list
    if not isinstance(numbers, list):
        valid = False

    # Check if numbers is not empty
    if valid and len(numbers) == 0:
        valid = False
    
    if valid:
        # Loop through numbers
        for number in numbers:

            # Check if number is an integer
            if not isinstance(number, (int, float)):
                valid = False
                break
    
    # Return valid
    return valid