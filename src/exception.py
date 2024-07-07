import sys
import os
from logger import logging

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'S:/NEW/Projects/KN_ETE_ML_Project/')))
from src.logger import logging

def error_message_detail(error, error_details:sys):
    _,_,exc_tb = error_details.exc_info()
    filename = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    e = str(error)

    error_msg = f"Error occured in python script name {filename} at line number {line_number} : error message {e}"

    return error_msg


class CustomException(Exception):
    def __init__(self, error_msg, error_details:sys):
        super().__init__(error_msg)
        self.error_msg = error_message_detail(error_msg, error_details=error_details)
    
    def __str__(self):
        return self.error_msg
    

print("Exception file worked")

# if __name__ == "__main__":
#     try:
#         a=1/0
#     except Exception as e:
#         logging.info('Divide By Zero')
#         raise CustomException(e,sys)



