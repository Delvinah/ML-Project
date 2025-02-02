import sys
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO)

def error_details(error, error_detail:sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = 'Error occurred in script name [{0}] line number [{1}] error message [{2}]'.format(
        file_name, exc_tb.tb_lineno, str(error))
    return error_message  # Ensure this returns the error message

class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_details(error_message, error_detail)  # Get the error details

    def __str__(self):
        return self.error_message  # Return the custom error message

if __name__ == "__main__":
    try:
        a = 1 / 0  # This will raise a ZeroDivisionError
        
    except Exception as e:
        logging.info("Divide by zero error occurred")  # Log the info message
        raise CustomException(e, sys)  # Raise the custom exception
