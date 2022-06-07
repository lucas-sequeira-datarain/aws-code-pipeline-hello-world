# METHODS

def sum_numbers(numbers: list) -> bool:
    """
    Sums a list of numbers.

    Params:
    -------
        numbers (list): list of numbers

    Returns:
    --------
        int: sum of numbers
    """

    # Initialize sum
    sum = 0

    # Loop through numbers
    for number in numbers:
        sum += number

    # Return sum
    return sum