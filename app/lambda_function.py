# LIBS
from src.sum import sum_numbers
from src.validator import validate_list_of_numbers

# HANDLER
def lambda_handler(event, context):

    # Retrieve numbers from event
    numbers = event.get('numbers')

    # Validate numbers
    is_valid = validate_list_of_numbers(numbers)

    # Return not valid
    if not is_valid:
        return {
            'statusCode': 400,
            'body': 'Invalid list of numbers'
        }
    
    # Calculate sum
    sum = sum_numbers(numbers)

    # Return sum
    return {
        'statusCode': 200,
        'body': str(sum)
    }
